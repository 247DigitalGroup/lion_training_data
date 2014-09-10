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
import hashlib


def master_run():
    """ scheduling news_spider to all sitess """

    for cat in categories:
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
    f_train = open('%s/train_file' % path, 'w')
    f_test = open('%s/test_file' % path, 'w')
    for i, cat in enumerate(categories):
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
                f_train.write(str(i + 1) + '\t'+ body)
            for each in test:
                body = normalize_body(each['body'])
                f_test.write(str(i + 1) + '\t'+ body)
    f_train.close()
    f_test.close()


def count_data():
    """ build data set """

    for cat in categories:
        count = db.links.find({'category': cat['category']}).count()
        print cat['category'], count


def remove_duplicates():
    """ remove duplicates """
    import hashlib
    # from collections import Counter

    def get_final_data(seen, data):
        """ get unique data """
        final_data = []
        for line in data:
            category = line.split('\t')[0].strip()
            body = ''.join(line.split('\t')[1:]).strip()
            hash_value = hashlib.md5(body).hexdigest()
            if hash_value not in seen:
                final_data.append(category + '\t' + body + '\n')
                seen.add(hash_value)
        return final_data

    def write_data(path, data):
        """ write out data """
        f_write = open(path, 'w')
        for each in data:
            f_write.write(each)
        f_write.close()

    path = 'news_crawler/data/training_data/1'
    f_train = open('%s/train_file' % path, 'r')
    f_test = open('%s/test_file' % path, 'r')
    seen = set()
    final_train = get_final_data(seen, f_train)
    final_test = get_final_data(seen, f_test)
    print len(final_train), len(final_test)
    write_data('%s/train_file_truncated' % path, final_train)
    write_data('%s/test_file_truncated' % path, final_test)

    # dups_count = len(set(encoded_train) & set(encoded_test))
    # self_duplicates_train = [k for k, v in Counter(encoded_train).items() if v > 1]
    # print 'duplicates in training data(itself):', len(
    #     self_duplicates_train), 'of', len(encoded_train)
    # self_duplicates_test = [k for k, v in Counter(encoded_test).items() if v > 1]
    # print 'duplicates in testing data(itself):', len(
    #     self_duplicates_test), 'of', len(encoded_test)
    # print 'duplicates of testing in training data:', dups_count, 'of', len(
    #     encoded_test), 'in', len(encoded_train)





if __name__ == '__main__':
    # news_spider('Vehicles')
    # master_run()
    # build_data()
    count_data()
    # remove_duplicates()
