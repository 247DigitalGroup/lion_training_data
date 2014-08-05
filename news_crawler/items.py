# -*- coding: utf-8 -*-

""" defines items """

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ArticleItem(Item):
    """ article item """

    link = Field()
    categories = Field()
