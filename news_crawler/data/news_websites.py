# -*- coding: utf-8 -*-

""" contains news websites associated with category links """


NEWS_WEBSITES = [
    # {
    #     'homepage': 'http://mashable.com/',
    #     'category_xpath': '//li[@class="collapsable channel submenu"]/a/@href',
    #     'article_xpath': ['//h1[@class="article-title"]/a/@href'],
    #     'category_regex': '.+/(.+)/'
    # },
    {
        'homepage': 'http://edition.cnn.com/',
        'category_xpath': '//ul[@id="intl-menu"]/li/a/@href',
        'article_xpath': '//a[@target="_self"]/@href',
        'regex': {
            'article': '.+/([a-z-]+)/([a-z-]+)/.+.html',
            'category': '/([A-Z]+)/'
        },
        'ignored': ['video']
    },
    {
        'homepage': 'http://www.huffingtonpost.com/',
        'category_xpath': '//a[@class="topnav_tab_link"]/@href',
        'article_xpath': [
            '//div[@class="most_popular_entry"]/a/@href',
            '//div[@class="entry"]/h4/a/@href',
            '//div[@class="col entry_right"]/h3/a/@href'
        ],
        'regex': {
            'article': 'ref=([a-z-]+)'
        }
    },
    {
        'homepage': 'http://www.nytimes.com/',
        'category_xpath': '//ul[@class="mini-navigation-menu"]/li/a/@href',
        'article_xpath': '//div[@class="story"]/h3/a/@href',
        'regex': {
            'article': '.+/(.+)/.+.html'
        }
    },
    {
        'homepage': 'http://www.theguardian.com/',
        'category_xpath': '//ul[@class="local-nav related-to-crumb1"]/li/a/@href',
        'article_xpath': '//div[@class="bd"]//a[@class="link-text"]/@href',
        'regex': {
            'category': '.com/([a-z-]+)/.+'
        }
    },
    {
        'homepage': 'http://www.businessinsider.com/',
        'category_xpath': '//div[@class="main-nav"]/ul/li/a/@href',
        'article_xpath': [
            '//a[@class="title"]/@href',
            '//*[@id="content"]/div[3]/div[2]/div/ul/li/h4/a'
        ],
        'regex': {
            'category': '.com/(.+)'
        }
    },

]
