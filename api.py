""" implements APIs """

import requests
import simplejson as json

# pylint: disable=E1101,E1002,W0702

def get_topic_id(category=None):
    """ get topic id """

    # url = 'http://api.clicklion.net/topics'
    # headers = {'Authorization': 'Token token="add7f5dd104645676a0c7a21d47bacaf"'}
    # response = requests.get(url, headers=headers)
    # try:
    #     response = dict(json.loads(response.text))
    # except:
    #     print response.text
    response = {u'17': u'Sports & Fitness', u'15': u'Arts & Entertainment', u'14': u'Finance', u'11': u'Law & Government', u'10': u'Vehicles', u'13': u'Apparel', u'12': u'Food & Groceries', u'20': u'Education', u'21': u'Health', u'22': u'Business & Industrial', u'16': u'Family & Community', u'19': u'Digital Technology', u'18': u'Home & Garden', u'1': u'Retailers & General Merchandise', u'3': u'Media & Publications', u'2': u'Dining & Nightlife', u'5': u'Telecom', u'4': u'Real Estate', u'7': u'Jobs & Education', u'6': u'Occasions & Gifts', u'9': u'Beauty & Personal Care', u'8': u'Travel & Tourism'}
    # print response
    for topic_id, topic in response.iteritems():
        if topic.lower() == category.lower():
            return topic_id
    return -1


if __name__ == '__main__':
    print get_topic_id('Jobs & Education')
