# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from jianshu.MysqlTools import MysqlTools, MysqlTools_Twisted

class JianshuPipeline(object):
    def __init__(self):
        self.mysqltool = MysqlTools()
        self.mysqltool.createDB()
        self.mysqltool.createTable()
    
    def process_item(self, item, spider):
        self.mysqltool.insert(item)
        return item

class JianshuPipeline_Twisted(object):
    def __init__(self):
        self.mysqltool_twisted = MysqlTools_Twisted()
    
    def process_item(self, item, spider):
        self.mysqltool_twisted.insert_item(item)
        return item