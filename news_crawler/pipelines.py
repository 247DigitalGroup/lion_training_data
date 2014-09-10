# -*- coding: utf-8 -*-

""" scrapy's pipelines """


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from news_crawler.settings import db, local_redis
from news_crawler.items import ArticleItem
from datetime import datetime
import hashlib
from scrapy.exceptions import DropItem


class DuplicatesPipeline(object):
    """ to make sure categories is not empty """

    # def __init__(self, *args, **kwargs):
    #     self.seen = set()
    #     for row in db.links.find():
    #         value = hashlib.md5(row['body'].encode('utf8')).hexdigest()
    #         if value in self.seen:
    #             db.links.remove({'_id': row['_id']})
    #         else:
    #             self.seen.add(value)

    @classmethod
    def process_item(cls, item, spider):
        """ global processor """

        value = hashlib.md5(item['body'].encode('utf8')).hexdigest()
        result = local_redis.set('training_data_seen', value)
        if not result:
            raise DropItem()
        return item


class NewsCrawlerPipeline(object):
    """ implements methods for storing/updating article data """

    def __init__(self, *args, **kwargs):
        for row in db.links.find():
            value = hashlib.md5(row['body'].encode('utf8')).hexdigest()
            local_redis.sadd('training_data_seen', value)

    def process_item(self, item, spider):
        """ global processor """

        if isinstance(item, ArticleItem):
            self.process_article(item)
        return item

    @classmethod
    def process_article(cls, item):
        """ handles article items """

        doc = dict(item)
        _id = hashlib.sha1(doc['body'].encode('utf8')).hexdigest()
        result = local_redis.sadd('training_data_seen', _id)
        if not result:
            return
        doc['created_at'] = datetime.now()
        fields = {key: value for (key, value) in doc.iteritems()}
        db.links.update({'_id': _id}, {'$set': fields}, upsert=True)
