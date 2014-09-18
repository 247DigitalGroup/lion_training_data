# -*- coding: utf-8 -*-

""" Scrapy settings for news_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
"""

BOT_NAME = 'news_crawler'
# LOG_LEVEL = 'INFO'
# DOWNLOAD_DELAY = 1
MAX_ITEMS = 10000
SPIDER_MODULES = ['news_crawler.spiders']
NEWSPIDER_MODULE = 'news_crawler.spiders'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'news_crawler.middlewares.RandomUserAgentMiddleware': 400,
    'news_crawler.middlewares.CustomDownloaderMiddleware': 500
}

ITEM_PIPELINES = {
    # 'news_crawler.pipelines.DuplicatesPipeline': 100,
    'news_crawler.pipelines.NewsCrawlerPipeline': 200,
}

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko)\
    Chrome/22.0.1207.1 Safari/537.1',
    'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 \
    (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko)\
    Chrome/20.0.1092.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko)\
    Chrome/20.0.1090.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko)\
    Chrome/19.77.34.5 Safari/537.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko)\
    Chrome/19.0.1084.9 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko)\
    Chrome/19.0.1084.36 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko)\
    Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko)\
    Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3\
    (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)\
    Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko)\
    Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)\
    Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko)\
    Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko)\
    Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)\
    Chrome/19.0.1061.0 Safari/536.3',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko)\
    Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24\
    (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'
]

DB_HOST = '127.0.0.1'
DB_PORT = 27017
DB_NAME = 'lion_training_data_2'

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
LOCAL_DB = 14

from pymongo import MongoClient
import redis

try:
    from local_settings import *
except:
    pass

db = MongoClient(DB_HOST, DB_PORT)
db = db[DB_NAME]
local_redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=LOCAL_DB)
