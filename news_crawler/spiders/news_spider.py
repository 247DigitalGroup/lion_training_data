# -*- coding: utf-8 -*-

""" implements news spider class """

# pylint: disable=E1101,E1002,W0702

from scrapy.spider import Spider
from scrapy.http.request import Request
from scrapy.http import HtmlResponse
from scrapy import log
from news_crawler.data.categories import CATEGORIES as categories
from news_crawler.items import ArticleItem
from news_crawler.loaders import DefaultItemLoader
from news_crawler.settings import MAX_ITEMS
import news_crawler.spiders.utils as utils
from scrapy.contrib.linkextractors import LinkExtractor
import re
import Levenshtein
from goose import Goose


class NewsSpider(Spider):
    """ crawls articles from news websites associated with categories """

    name = "data"
    settings = {
        'LOG_LEVEL': 'INFO',
        'CLOSESPIDER_ITEMCOUNT': MAX_ITEMS,
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'DOWNLOAD_TIMEOUT': 30,
        'COOKIES_ENABLED': False,
        'RETRY_ENABLED': False,
        'REDIRECT_ENABLED': True,
        'REDIRECT_MAX_TIMES': 1,
        'AJAXCRAWL_ENABLED': True,
    }

    def __init__(self, *args, **kwargs):
        super(NewsSpider, self).__init__(*args, **kwargs)
        self.link = kwargs.get('link', None)
        self.category = kwargs.get('category', None)
        self.allowed_domains = set()
        self.max_items_per_domain = 0

    @classmethod
    def from_crawler(cls, crawler, **spider_kwargs):
        """ overrides crawler's settings """

        settings = crawler.settings
        for key, value in cls.settings.iteritems():
            settings.set(key, value)
        return cls(**spider_kwargs)

    @classmethod
    def get_site_by_link(cls, link):
        """ retrieve site from a link """

        for cat in categories:
            for site in cat['data']:
                if site['link'] == link:
                    return site

    @classmethod
    def get_category_by_link(cls, link):
        """ retrieve category from a link """

        for category in categories:
            for site in category['data']:
                if site['link'] == link:
                    return category['category']

    @classmethod
    def get_sites_by_category(cls, category):
        """ retrieve sites from a category """

        for cat in categories:
            if cat['category'] == category:
                return cat['data']

    def start_requests(self):
        if self.link:
            site = self.get_site_by_link(self.link)
            domain = utils.url_to_domain(self.link)
            self.allowed_domains = [domain]
            site['domain'] = domain
            self.category = self.get_category_by_link(self.link)
            yield Request(
                self.link, callback=self.parse_article, meta={'site': site, 'select': False})
        else:
            sites = self.get_sites_by_category(self.category)
            for site in sites:
                domain = utils.url_to_domain(site['link'])
                self.allowed_domains.add(domain)
                site['domain'] = domain
                yield Request(
                    site['link'], callback=self.parse_article, meta={'site': site, 'select': False})

    def parse(self, response):
        pass

    @classmethod
    def is_valid(cls, response):
        """ if the response is valid """

        if not isinstance(response, HtmlResponse):
            log.msg('[%s X] - %s' % (
                str(response.status), response.url), level=log.INFO)
            return

        site = response.request.meta['site']
        new_domain = utils.url_to_domain(response.url)
        if new_domain != site['domain']:
            return

        log.msg('[%s] - %s' % (
            str(response.status), response.url), level=log.INFO)

        return True

    def _extract_links(self, response, params):
        """ parse links from response
            @return hrefs
        """

        params['allow_domains'] = tuple(self.allowed_domains)
        link_extractor = LinkExtractor(**params)
        return link_extractor.extract_links(response)

    @classmethod
    def filter_links_by_regex(cls, links, regex):
        """ filter links """
        final_links = []
        for link in links:
            if re.search(regex, link.url):
                final_links.append(link)
        return final_links

    @classmethod
    def deny_links(cls, links, regex):
        """ filter links """
        final_links = []
        for link in links:
            if not re.search(regex, link.url):
                final_links.append(link)
        return final_links

    @classmethod
    def acceptable_body(cls, body):
        """ Accepts body of equal or greater than 100 characters """

        if not body or len(body) < 100:
            return False
        return True

    def parse_article(self, response):
        """ parse article pages from response """

        if not self.is_valid(response):
            return

        site = response.request.meta['site']

        links = self._extract_links(response, {
            'allow': site.get('regex', ()),
            'restrict_xpaths': site.get('xpath', ())})
        for link in links:
            yield Request(link.url, callback=self.parse_article, meta={
                'site': site, 'select': True})
        if 'follow' in site:
            links = self._extract_links(response, {
                'restrict_xpaths': site['follow']})
            for link in links:
                yield Request(link.url, callback=self.parse_article, meta={
                    'site': site, 'select': False})

        if response.request.meta['select']:
            loader = DefaultItemLoader(item=ArticleItem(), response=response)
            loader.add_value('link', response.url)
            loader.add_value('category', self.category)
            loader = self.parse_content(response.body, loader)

            if not self.acceptable_body(loader.get_output_value('body')):
                return

            yield loader.load_item()


    # @classmethod
    # def extract_title(cls, loader):
    #     """ extract title """

    #     loader.add_xpath(
    #         'raw_title', '//h1//text() | //h2//text() | //h3//text()')

    # @classmethod
    # def choose_best_title(cls, loader, title_hint, candidates):
    #     """ choose the best title from candidates """

    #     for title in candidates:
    #         ratio = Levenshtein.ratio(title_hint, title)
    #         if ratio > 0.8:
    #             # print title, '---', title_hint
    #             loader.replace_value('title', title)
    #             return

    @classmethod
    def parse_content(cls, html, loader):
        """ parse content(title, body) from html """

        try:
            goose_obj = Goose()
            article = goose_obj.extract(raw_html=html)
            loader.add_value('body', article.cleaned_text)
        except:
            pass
        return loader
        # self.extract_title(loader)
        # self.choose_best_title(
        #     loader, article.title, loader.get_collected_values('raw_title'))
