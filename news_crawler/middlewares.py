# -*- coding: utf8 -*-

""" Scrapy middlewares """

# pylint: disable=W0232,W0613
# !/usr/bin/env python
# -*- coding: utf8 -*-

import random
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from news_crawler.settings import USER_AGENTS
from scrapy.exceptions import IgnoreRequest
import news_crawler.spiders.utils as utils


class RandomUserAgentMiddleware(UserAgentMiddleware):
    """ randomize user agent string """

    @classmethod
    def process_request(cls, request, spider):  # pylint: disable=W0613
        user_agent = random.choice(USER_AGENTS)
        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)


class CustomDownloaderMiddleware(object):
    """ ignore a few extensions """

    @classmethod
    def process_response(cls, request, response, spider):
        """ handle response """

        if not utils.is_english(response.body):
            raise IgnoreRequest()
        return response
