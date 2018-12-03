# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import scrapy.FormRequest, scrapy.Request


class HongniangspiderSpider(CrawlSpider):
    name = 'HongNiangSpider'
    allowed_domains = ['hongniang.com']
    start_urls = ['http://www.hongniang.com/index/search?sort=0&wh=0&sex=2&starage=0&province=上海&city=0']

    rules = (
        Rule(LinkExtractor(allow=r'/user/member.id/\d+', restrict_xpaths='//li[@class="pin"]'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'page=\d+', restrict_xpaths='//a[@class="next"]'), follow=True),        
    )

    def parse_item(self, response):
        if '详细资料' in response.text:
            age = response.xpath('//div[@class="info2"]/div/ul/li[1]/child::node()[2]').extract_first().strip()
            ismarried = response.xpath('//div[@class="info2"][1]/div/ul/li[2]/child::node()[2]').extract_first().strip()
            height = response.xpath('//div[@class="info2"]/div/ul/li/span[text()="身高："]/../text()').extract_first().strip()
#             height2 = response.xpath('//div[@class="info2"]/div/ul/li[./span/text()="身高："]/text()').extract_first().strip()
            education = response.xpath('//div[@class="info2"]/div/ul/li/span[text()="学历："]/../text()').extract_first()
            yearincome = response.xpath('//div[@class="info2"]/div/ul/li[./span/text()="年收入："]/text()').extract_first().strip()
            workplace = response.xpath('//div[@class="info2"]/div/ul/li/span[text()="工作地："]/../child::node()[2]').extract_first().strip() 
            monologue = response.xpath('//div[@class="info5"]/div[@class="tit"]/../div[@class="text"]/text()').extract_first().strip()
            
            print(age, ismarried, height, education, yearincome, workplace, monologue)
            




