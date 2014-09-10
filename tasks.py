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
import api


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


def write_data(f_write, topic_id, data):
    """ write out data """
    for each in data:
        body = normalize_body(each['body'])
        f_write.write(str(topic_id) + '\t'+ body)

def check_duplicates():
    """ check duplicates in db """
    rows = db.links.find()
    seen = set()
    count = 0
    for row in rows:
        value = hashlib.md5(row['body'].encode('utf8')).hexdigest()
        if value in seen:
            count += 1
            print row['category'], row['_id']
        else:
            seen.add(value)
    print count


def build_data():
    """ build data set """

    print "Building data set...\n"

    ratio = 0.8
    quantity = 1000
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
                {'category': cat['category'], 'body': {'$exists': True}}).limit(quantity)
            data = list(data)
            if len(data) < int(ratio*quantity):
                print 'DROPPED', cat['category'], len(data)
                continue
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


# def remove_duplicates():
#     """ remove duplicates """
#
#     def get_final_data(seen, data):
#         """ get unique data """
#         final_data = []
#         for line in data:
#             category = line.split('\t')[0].strip()
#             body = ''.join(line.split('\t')[1:]).strip()
#             hash_value = hashlib.md5(body).hexdigest()
#             if hash_value not in seen:
#                 final_data.append(category + '\t' + body + '\n')
#                 seen.add(hash_value)
#         return final_data
#
#
#     path = 'news_crawler/data/training_data/1'
#     f_train = open('%s/train_file' % path, 'r')
#     f_test = open('%s/test_file' % path, 'r')
#     seen = set()
#     final_train = get_final_data(seen, f_train)
#     final_test = get_final_data(seen, f_test)
#     print len(final_train), len(final_test)
#     write_data('%s/train_file_truncated' % path, final_train)
#     write_data('%s/test_file_truncated' % path, final_test)

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
    count_data()
    # build_data()
    check_duplicates()
