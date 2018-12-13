# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiciItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    host = scrapy.Field()
    port = scrapy.Field()
    addr = scrapy.Field()
    ip_type = scrapy.Field()
    speed = scrapy.Field()
    connect = scrapy.Field()
    exits = scrapy.Field()
    verify = scrapy.Field()
    pass
