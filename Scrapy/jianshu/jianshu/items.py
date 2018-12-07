# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    avatar = scrapy.Field()
    athour = scrapy.Field()
    url = scrapy.Field()
    artile_id = scrapy.Field()
    publish_time = scrapy.Field()
    content = scrapy.Field()
