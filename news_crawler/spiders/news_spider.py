# -*- coding: utf-8 -*-

""" implements news spider class """

from scrapy.spider import Spider
from scrapy.http.request import Request
from scrapy.selector import Selector
from scrapy import log
from news_crawler.data.news_websites import NEWS_WEBSITES
from news_crawler.items import ArticleItem
from news_crawler.loaders import DefaultItemLoader
import re
from tld import get_tld
from scrapy.utils.url import canonicalize_url
import urlparse


class NewsSpider(Spider):
    """ crawls articles from news websites associated with categories """

    name = "news"

    def __init__(self, *args, **kwargs):
        super(NewsSpider, self).__init__(*args, **kwargs)
        self.link = kwargs.get('link', None)

    @classmethod
    def get_site_from_link(cls, link):
        """ retrieve site from a link """

        for site in NEWS_WEBSITES:
            if site['homepage'] == link:
                return site

    @classmethod
    def url_to_domain(cls, link):
        """ converts link to domain """

        try:
            return get_tld(link)
        except Exception:  # pylint: disable=W0703
            return None

    def start_requests(self):
        if self.link:
            site = self.get_site_from_link(self.link)
            yield Request(self.link, callback=self.parse_category, meta={'site': site})
        else:
            for site in NEWS_WEBSITES:
                yield Request(
                    site['homepage'], callback=self.parse_category, meta={'site': site})

    def parse(self, response):
        pass

    def parse_category(self, response):
        """ extract category links """

        log.msg('[%s] - %s' % (
            str(response.status), response.url), level=log.INFO)

        site = response.request.meta['site']
        selector = Selector(response)
        links = selector.xpath(site['category_xpath']).extract()
        for link in self.refine_links(links):
            link = urlparse.urljoin(response.url, link)
            yield Request(link, callback=self.parse_article, meta={'site': site})

    def parse_article(self, response):
        """ extract article links """

        log.msg('[%s] - %s' % (
            str(response.status), response.url), level=log.INFO)

        site = response.request.meta['site']
        categories = self.extract_categories(
            site['regex'].get('category', None), response.url)
        selector = Selector(response)
        if not isinstance(site['article_xpath'], list):
            site['article_xpath'] = [site['article_xpath']]
        for xpath in site['article_xpath']:
            links = selector.xpath(xpath).extract()
            for link in self.refine_links(links):
                link = urlparse.urljoin(response.url, link)
                yield Request(link, callback=self.extract_article, meta={
                    'site': site, 'categories': categories})

    def extract_article(self, response):
        """ extract categories and creates an article item """

        log.msg('[%s] - %s' % (
            str(response.status), response.url), level=log.INFO)

        site = response.request.meta['site']
        categories = self.extract_categories(
            site['regex'].get('article', None), response.url)
        categories += response.request.meta['categories']
        loader = DefaultItemLoader(item=ArticleItem(), response=response)
        loader.add_value('link', response.url)
        loader.add_value('categories', set(categories))
        yield loader.load_item()

    @classmethod
    def refine_links(cls, links):
        """ refines links to avoid duplicates """

        refine_links = set([canonicalize_url(link) for link in links])
        return refine_links

    @classmethod
    def extract_categories(cls, regex, link):
        """ extracts categories from link """

        if not regex:
            return []

        categories = []
        match = re.search(regex, link)
        if match:
            categories.append(match.group(1))
        print regex, link, categories

        return categories

