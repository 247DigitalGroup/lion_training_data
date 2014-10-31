""" scheduling tasks """

# pylint: disable=E1101

from datetime import datetime
import requests
try:
    import simplejson as json
except ImportError:
    import json
from news_crawler.data.categories import CATEGORIES as categories
from news_crawler.settings import db, local_redis
from news_crawler.settings import MAX_ITEMS
import os
import time
import hashlib
import api
import random


def master_run():
    """ scheduling news_spider to all sitess """

    for cat in categories:
        count = db.links.find({'category': cat['category']}).count()
        if count < 10000:
            news_spider(cat['category'])


def news_spider(category):
    """ schedule news_spider """

    payload = {
        'project': 'news_crawler',
        'spider': 'data',
        'category': category
    }
    req = requests.post('http://localhost:6800/schedule.json', data=payload)
    result = json.loads(req.text)
    result['spider'] = 'data'
    result['created_at'] = datetime.now()
    print result


def normalize_body(body):
    """ remove \n \r in body """
    body = body.replace('\n', ' ').replace('\r', '')
    return body.encode('utf8').strip() + '\n'


def write_data(f_write, topic_id, data):
    """ write out data """
    for each in data:
        body = normalize_body(each['body'])
        f_write.write(str(topic_id) + '\t' + body)


def check_duplicates():
    """ check duplicates in db """
    print "Building data set...\n"

    rows = db.links.find()
    seen = set()
    count = 0
    for row in rows:
        value = hashlib.md5(row['body'].encode('utf8')).hexdigest()
        if value in seen:
            count += 1
            print row['category'], row['_id']
            # db.links.remove({'_id': row['_id']})
        else:
            seen.add(value)
    print count, 'duplicate(s)'
    print "-------------------\n"


def build_data():
    """ build data set """

    print "Building data set...\n"

    ratio = 0.8
    quantity = 10000
    path = 'news_crawler/data/training_data/%s' % time.strftime('%d-%m-%Y %H%M%S')
    os.makedirs(path, 0755)
    f_train = open('%s/train_file' % path, 'ab')
    f_test = open('%s/test_file' % path, 'ab')
    for cat in categories:
        if cat['data'] is not None:
            topic_id = api.get_topic_id(cat['category'])
            if topic_id == -1:
                print "Cannot get topic id: ", cat['category']
                continue
            data = db.links.find(
                {'category': cat['category'], 'body': {'$exists': True}})#.limit(quantity)
            data = list(data)
            random.shuffle(data)
            data = data[:quantity]
            # if len(data) < int(ratio*quantity):
            #     print 'DROPPED', cat['category'], len(data)
            #     continue
            print cat['category'], len(data)
            train_data = data[:int(ratio*len(data))]
            test_data = data[int(ratio*len(data)):]
            write_data(f_train, topic_id, train_data)
            write_data(f_test, topic_id, test_data)
    f_train.close()
    f_test.close()
    print "-------------------\n"


def count_data():
    """ build data set """

    print "Counting data quantity...\n"

    for cat in categories:
        count = db.links.find({'category': cat['category']}).count()
        print cat['category'], count
    print "-------------------\n"


def push_seen_data_to_redis():
    """ push seen data to redis """

    for row in db.links.find():
        value = hashlib.md5(row['body'].encode('utf8')).hexdigest()
        local_redis.sadd('training_data_seen', value)


def make_md5():
    for row in db.links.find():
        doc = dict(row)
        del doc['_id']
        _id = hashlib.md5(row['body'].encode('utf8')).hexdigest()
        fields = {key: value for (key, value) in doc.iteritems()}
        db.new_links.update({'_id': _id}, {'$set': fields}, upsert=True)


def review():
    f = open('predict_results.txt', 'rb')
    results = []
    for line in f:
        body = ' '.join(line.split(' ')[2:]).strip()
        body_part = body[:20]
        if not body_part:
            continue
        print body_part
        result = db.links.find({'body': {'$regex': body_part}}).limit(1)
        try:
            results.append(result[0]['link'])
            print body_part, result[0]['link']
        except:
            continue
    f.close()
    f = open('results.txt', 'wb')
    for each in results:
        f.write(each + '\n')
    f.close()





if __name__ == '__main__':
    # push_seen_data_to_redis()

    # news_spider('Home & Garden')
    # master_run()
    count_data()
    # check_duplicates()
    # build_data()
    # make_md5()
    # review()
