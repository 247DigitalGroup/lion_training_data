""" implements APIs """

import requests
import simplejson as json

# pylint: disable=E1101,E1002,W0702

def get_topic_id(category=None):
    """ get topic id """

    url = 'http://api.clicklion.net/topics'
    headers = {'Authorization': 'Token token="add7f5dd104645676a0c7a21d47bacaf"'}
    response = requests.get(url, headers=headers)
    response = dict(json.loads(response.text))
    for topic_id, topic in response.iteritems():
        if topic.lower() == category.lower():
            return topic_id
    return -1

if __name__ == '__main__':
    print get_topic_id('health')
