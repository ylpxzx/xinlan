# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XinlanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    table = 'xinlan_english'#Mysql表
    title=scrapy.Field()
    news_url=scrapy.Field()
    time=scrapy.Field()
    content=scrapy.Field()
