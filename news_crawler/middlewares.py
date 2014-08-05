# -*- coding: utf8 -*-

""" Scrapy middlewares """

# pylint: disable=W0232,W0613
# !/usr/bin/env python
# -*- coding: utf8 -*-

import random
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from news_crawler.settings import USER_AGENTS


class RandomUserAgentMiddleware(UserAgentMiddleware):
    """ randomize user agent string """

    @classmethod
    def process_request(cls, request, spider):  # pylint: disable=W0613
        user_agent = random.choice(USER_AGENTS)
        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)
