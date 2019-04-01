# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScientificItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    subject_name = scrapy.Field()
    subject_url = scrapy.Field()
    subject_indexes = scrapy.Field()
