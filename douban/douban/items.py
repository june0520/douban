# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    #设置MONGO的表名称
    collection = 'movie'
    name = scrapy.Field()
    db = scrapy.Field()
    star = scrapy.Field()
    quote = scrapy.Field()
