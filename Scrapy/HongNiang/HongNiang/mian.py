'''
Created on 2018年11月14日

@author: cy
'''
from scrapy import cmdline

cmd = 'scrapy crawl HongNiangSpider'
cmdline.execute(cmd.split())