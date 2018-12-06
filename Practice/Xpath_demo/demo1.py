'''
Created on 2018年11月30日

@author: cy
'''
    
from lxml import etree 

html1 = etree.parse('1.html')
print(html1.xpath('//div[@id="B"]/div[2]/attribute::*'))
print(html1.xpath("//div[@id='child2']/../@id"))
print(html1.xpath("//div[@id='child2']/../div[@id='child1']/text()"))
print(html1.xpath("//div[@id='B']/div[@price>100]/../node()"))
print(html1.xpath("//div[@price>100]/../self::node()/@id"))
print(html1.xpath("//div[@price>100]/../node()/text()"))
print(html1.xpath("//div[@price>100]/../child::node()/text()"))
print(html1.xpath("//div[@id='child1']/../div[position()>1 and position()<3]/text()"))
print(html1.xpath("//div[@price='200']/../div[last()]/text()"))
print(html1.xpath("//div[@price='200']/../div[last()-1]/text()"))