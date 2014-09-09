""" scheduling tasks """

# pylint: disable=E1101

from datetime import datetime
import requests
try:
    import simplejson as json
except ImportError:
    import json
from news_crawler.data.categories import CATEGORIES as categories
from news_crawler.settings import db
import os
import time


def master_run():
    """ scheduling news_spider to all sitess """

    for cat in categories:
        for site in cat['data']:
            news_spider(site['link'])


def run_by_category(category):
    """ scheduling news_spider to all sitess """

    for cat in categories:
        if category and cat['category'] == category:
            for site in cat['data']:
                news_spider(site['link'])
            break


def news_spider(link):
    """ schedule news_spider """

    payload = {
        'project': 'news_crawler',
        'spider': 'data',
        'link': link
    }
    req = requests.post('http://localhost:6800/schedule.json', data=payload)
    result = json.loads(req.text)
    result['spider'] = 'news'
    result['created_at'] = datetime.now()
    print result


def normalize_body(body):
    """ remove \n \r in body """
    body = body.replace('\n', ' ').replace('\r', '')
    return body.encode('utf8').strip() + '\n'


def build_data():
    """ build data set """

    ratio = 0.8
    quantity = 10000
    path = 'news_crawler/data/training_data/%s' % time.strftime('%d-%m-%Y %H%M%S')
    os.makedirs(path, 0755)
    f_train = open('%s/train' % path, 'w')
    f_test = open('%s/test' % path, 'w')
    for cat in categories:
        if cat['data'] is not None:
            data = db.links.find(
                {'category': cat['category'], 'body': {'$exists': True}}).limit(quantity)
            data = list(data)
            if len(data) < int(ratio*quantity):
                print 'DROPPED', cat['category'], len(data)
                continue
            print cat['category'], len(data)
            train = data[:int(ratio*len(data))]
            test = data[int(ratio*len(data)):]
            for each in train:
                body = normalize_body(each['body'])
                f_train.write(cat['category'].encode('utf8') + '\t'+ body)
            for each in test:
                body = normalize_body(each['body'])
                f_test.write(cat['category'].encode('utf8') + '\t'+ body)
    f_train.close()
    f_test.close()

if __name__ == '__main__':
    # master_run()
    build_data()
