# !/usr/bin/env python
# -*- coding: utf-8 -*-

""" helpers """

import unicodedata
from tld import get_tld
import urlparse
from scrapy.utils.url import canonicalize_url
import langid


def domain_to_url(domain):
    """ converts domain to an url """
    try:
        domain = get_tld(domain)
    except Exception:  # pylint: disable=W0703,W0704
        pass
    return 'http://www.' + domain + '/'


def url_to_domain(url):
    """ converts links to domain """
    try:
        return get_tld(url)
    except Exception:  # pylint: disable=W0703
        return None


def is_absolute(url):
    """ check if an url is absolute """
    return bool(urlparse.urlparse(url).netloc)


def normalize_url(root_link, link):
    """ refine an url """
    link = canonicalize_url(link)
    return urlparse.urljoin(root_link, link)


def normalize_unicode(str_data):
    """ normalize str characters into unicode """
    try:
        normalized = unicodedata.normalize('NFKD', unicode(str_data)).encode('ascii', 'ignore')
    except UnicodeError:
        normalized = unicode(str_data, 'ascii', 'ignore')
    return normalized

def is_english(text):
    """ if the html text is english """

    lang = langid.classify(text)
    if lang and 'en' in lang[0]:
        return True
    return False
