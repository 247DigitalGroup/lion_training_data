# -*- coding: utf-8 -*-

"""This file is written for Scrapy's processors."""

# pylint: disable=E1101,E1002,W0232


from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, Identity


class DefaultItemLoader(ItemLoader):
    """ default loader for itemss."""

    default_output_processor = TakeFirst()
    categories_out = Identity()

    def add_value(self, field_name, value):
        super(DefaultItemLoader, self).add_value(field_name, value)

    def load_item(self):
        return super(DefaultItemLoader, self).load_item()
