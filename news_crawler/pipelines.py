# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from news_crawler.settings import db
from news_crawler.items import ArticleItem
from datetime import datetime
import hashlib
from scrapy.exceptions import DropItem


class ValidateCategoriesPipeline(object):
    """ to make sure categories is not empty """

    @classmethod
    def process_item(cls, item, spider):
        """ global processor """

        if len(item.get('categories', [])) == 0:
            raise DropItem('categories empty: %s' % item['link'])
        return item


class NewsCrawlerPipeline(object):
    """ implements methods for storing/updating article data """

    def process_item(self, item, spider):
        """ global processor """

        if isinstance(item, ArticleItem):
            self.process_article(item)
        return item

    @classmethod
    def process_article(cls, item):
        """ handles article items """

        doc = dict(item)
        _id = hashlib.sha1(doc['link']).hexdigest()
        result = db.links.find({'_id': _id}, {'_id': 1}).limit(1).count()
        if result:
            doc['last_modified'] = datetime.now()
        else:
            doc['created_at'] = datetime.now()
        fields = {key: value for (key, value) in doc.iteritems()}
        db.links.update({'_id': _id}, {'$set': fields}, upsert=True)
