# -*- coding: utf-8 -*-

""" contains news websites associated with category links """


NEWS_WEBSITES = [
    # {
    #     'homepage': 'http://www.huffingtonpost.com/',
    #     'article_regex': 'ref=(.+)',
    #     'blacklist_regex': 'mostpopular'
    # },
    {
        'homepage': 'http://www.foxnews.com/',
        'article_regex': '.+/(.+)/[0-9]{4}/',
        'blacklist_regex': 'nation.foxnews.com'
    },
    {
        'homepage': 'http://usatoday.com/',
        'article_regex': 'com/[^/]+/([^/]+)/.+/[0-9]+'
    },
    {
        'homepage': 'http://edition.cnn.com/',
        'article_regex': '/[0-9]+/[0-9]+/[0-9]+/(.+)/[^/]+/.+.html',
    },
    # {
    #     'homepage': 'http://www.nytimes.com/',
    #     'article_regex': '/[0-9]+/[0-9]+/[0-9]+/(.+)/[^/]+/.+.html',
    #     'blacklist_regex': [
    #         '.+/comments/.+'
    #     ]
    # },
    # {
    #     'homepage': 'http://www.theguardian.com/',
    #     'article_regex': 'http://www.theguardian.com/(.+)/[0-9]{4}/'
    # },
    # {
    #     'homepage': 'http://www.businessinsider.com/',
    #     'article_regex': '.+/(.+)/[0-9]{4}/'
    # },
    # {
    #     'homepage': 'http://www.washingtonpost.com/',
    #     'article_regex': 'com/([^/]+)',
    #     'blacklist_regex': [
    #         '/yellowpages',
    #         '/news',
    #         '/account',
    #         '/help',
    #         '/apps'
    #     ]
    # },

]

