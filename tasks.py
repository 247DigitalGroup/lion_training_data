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


def make_file_accessible(filepath, mode='w'):
    ''' Check if a file exists and is accessible. '''

    try:
        f = open(filepath, mode)
        f.close()
    except IOError:
        return False

    return True

def build_data():
    """ build data set """

    for cat in categories:
        if cat['data'] is not None:
            data = db.links.find(
                {'category': cat['category'], 'body': {'$exists': True}}).limit(10000)
            data = list(data)
            if len(data) < 8000:
                continue
            print cat['category'], len(data)
            train = data[:int(0.8*len(data))]
            test = data[int(0.8*len(data)):]
            train_path = 'news_crawler/data/training_data/train/%s' % cat['category']
            os.makedirs(train_path, 0755)
            test_path = 'news_crawler/data/training_data/test/%s' % cat['category']
            os.makedirs(test_path, 0755)
            for each in train:
                f_train = open('%s/%s' % (train_path, str(each['_id'])), 'w')
                f_train.write(each['body'].encode('utf8').strip())
                f_train.close()
            for each in test:
                f_test = open('%s/%s' % (test_path, str(each['_id'])), 'w')
                f_test.write(each['body'].encode('utf8').strip())
                f_test.close()


if __name__ == '__main__':
    # run_by_category('News, Media & Publications')
    master_run()
    # build_data()
