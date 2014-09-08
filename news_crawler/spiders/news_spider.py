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
        # 'LOG_LEVEL': 'DEBUG',
        'CLOSESPIDER_ITEMCOUNT': MAX_ITEMS,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 2,
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
                self.link, callback=self.parse_article, meta={'site': site})
        else:
            sites = self.get_sites_by_category(self.category)
            for site in sites:
                domain = utils.url_to_domain(site['link'])
                self.allowed_domains.add(domain)
                site['domain'] = domain
                yield Request(
                    site['link'], callback=self.parse_article, meta={'site': site})

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

    def _extract_links(self, response, restrict_xpaths=()):
        """ parse links from response
            @return hrefs
        """
        link_extractor = LinkExtractor(
            allow_domains=tuple(self.allowed_domains),
            restrict_xpaths=restrict_xpaths)
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


    def parse_article(self, response):
        """ parse article pages from response """

        if not self.is_valid(response):
            return

        site = response.request.meta['site']
        if site['select'][:1] == '//':
            links = self._extract_links(response, site['select'])
        else:
            links = self._extract_links(response)
        if 'deny' in site:
            links = self.deny_links(links, site['deny'])
        if site['select'] != 'all':
            links = self.filter_links_by_regex(links, site['select'])
        for link in links:
            yield Request(link.url, callback=self.parse_article, meta={
                'site': site})

        links = self._extract_links(response, site.get('follow', ()))
        if 'deny' in site:
            links = self.deny_links(links, site['deny'])
        for link in links:
            yield Request(link.url, callback=self.parse_article, meta={
                'site': site})

        loader = DefaultItemLoader(item=ArticleItem(), response=response)
        loader.add_value('link', response.url)
        loader.add_value('category', self.category)
        loader = self.parse_content(response.body, loader)

        yield loader.load_item()

    @classmethod
    def extract_title(cls, loader):
        """ extract title """

        loader.add_xpath(
            'raw_title', '//h1//text() | //h2//text() | //h3//text()')

    @classmethod
    def choose_best_title(cls, loader, title_hint, candidates):
        """ choose the best title from candidates """

        for title in candidates:
            ratio = Levenshtein.ratio(title_hint, title)
            if ratio > 0.8:
                # print title, '---', title_hint
                loader.replace_value('title', title)
                return

    def parse_content(self, html, loader):
        """ parse content(title, body) from html """

        self.extract_title(loader)
        goose_obj = Goose()
        try:
            article = goose_obj.extract(raw_html=html)
        except:
            return loader
        self.choose_best_title(
            loader, article.title, loader.get_collected_values('raw_title'))
        loader.add_value('body', article.cleaned_text)
        try:
            loader.add_value('image_url', article.top_image.src)
        except:
            pass
        return loader
