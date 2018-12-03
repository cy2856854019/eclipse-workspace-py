# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HongniangItem(scrapy.Item):

    #用户名称
    nickname = scrapy.Field()
    #用户id
    loveid = scrapy.Field()
    #用户的照片
    photos = scrapy.Field()
    #用户年龄
    age = scrapy.Field()
    #用户的身高
    height = scrapy.Field()
    #用户是否已婚
    ismarried = scrapy.Field()
    #用户年收入
    yearincome = scrapy.Field()
    #用户的学历
    education = scrapy.Field()
    #用户的地址
    workaddress= scrapy.Field()
    #用户的内心独白
    monologue = scrapy.Field()
    #用户的性别
    gender = scrapy.Field()
    
    