
# -*- coding: utf-8 -*-

""" implements news spider class """

# pylint: disable=E1101,E1002,W0702

from scrapy.http.request import Request
from scrapy import log
from news_crawler.items import ArticleItem
from news_crawler.spiders.news_spider import NewsSpider
import news_crawler.spiders.utils as utils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JSpider(NewsSpider):
    """ support to load more links by executing javascripts """

    name = "js"

    def __init__(self, *args, **kwargs):
        super(NewsSpider, self).__init__(*args, **kwargs)
        self.link = kwargs.get('link', None)
        self.allowed_domains = set()
        self.site = {}

    def start_requests(self):
        """ starting point """

        if not self.link:
            return
        domain = utils.url_to_domain(self.link)
        self.allowed_domains = [domain]
        site = self.get_site_by_link(self.link)
        site['domain'] = domain
        self.category = self.get_category_by_link(self.link)
        yield Request(
            site['link'], callback=self.load_more, meta={'site': site, 'select': False})

    def load_more(self, response):
        """ load more links """

        driver = webdriver.Chrome()
        driver.set_window_size(1280, 720)
        driver.get(response.url)
        while True:
            response = response.replace(body=driver.page_source)

            site = response.request.meta['site']
            links = self._extract_links(response, {
                'allow': site.get('regex', ()),
                'restrict_xpaths': site.get('xpath', ())})
            for link in links:
                yield Request(link.url, callback=self.parse_article, meta={
                    'site': site, 'select': True})
            if 'load_more' in site:
                wait = WebDriverWait(driver, 60)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, site['load_more'])))
                if element:
                    driver.find_element_by_xpath(site['load_more']).click()
                    driver.implicitly_wait(10)
                    continue
                else:
                    return
            return



