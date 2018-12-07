# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from jianshu.User_Agents import User_Agents
from jianshu.PROXY_IP import PROXY_IPS
import random


class JianshuDownloaderMiddleware(object):

    def process_request(self, request, spider):
        # 设置请求头和代理
        request.headers['User-Agent'] = random.choice(User_Agents)
#         request.meta['proxy'] = 'http://' + random.choice(PROXY_IPS)
        return None

    def process_response(self, request, response, spider):
        #返回码不是200 重新请求
        if response.status != 200:
            return request
        return response

