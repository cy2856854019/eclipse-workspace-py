# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from jianshu.User_Agents import User_Agents
from jianshu.PROXY_IP import PROXY_IPS
import random, time
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse

class JianshuDownloaderMiddleware(object):
    def __init__(self):
        firefoxoptions =  webdriver.FirefoxOptions()
        firefoxoptions.add_argument('--headless')
        self.driver = webdriver.Firefox()
    
    def process_request(self, request, spider):
        # 设置请求头和代理
#         request.headers['User-Agent'] = random.choice(User_Agents)
#         request.meta['proxy'] = 'http://' + random.choice(PROXY_IPS)
        self.driver.get(request.url)
        time.sleep(1)
        source = self.driver.page_source
        response = HtmlResponse(self.driver.current_url, body=source, request=request, encoding='utf-8')
        
        return response

    def process_response(self, request, response, spider):
        #返回码不是200 重新请求
        if response.status != 200:
            return request
        return response

