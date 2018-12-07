# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import ArticleItem


class JsspiderSpider(CrawlSpider):
    name = 'JsSpider'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']
    origion_url = 'https://www.jianshu.com'

    rules = (
        Rule(LinkExtractor(allow=r'/p/[0-9a-z]{12}'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.css('h1.title::text').get()
        avatar = self.origion_url + response.css('a.avatar::attr(href)').get()
        athour = response.css('div.author>div.info>span.name>a::text').get()
        url = response.url.split('?')[0]
        artile_id = url.split('/')[-1]
        publish_time = response.css('span.publish-time::text').get().replace('*', '')
        content = response.xpath('//div[@class="show-content-free"]').extract()
        
        item = ArticleItem(title=title, avatar=avatar, athour=athour, url=url, 
                           artile_id=artile_id, publish_time=publish_time, content=content)
        yield item
        
        
        