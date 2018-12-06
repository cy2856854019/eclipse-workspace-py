'''
Created on 2018年11月30日

@author: cy
'''
from queue import Queue
import threading, requests, re
from lxml import etree

class producer(threading.Thread):
    def __init__(self, page_queue, infor_queue, *args, **kargs):
        super().__init__(*args, **kargs)
        self.page_queue = page_queue
        self.infor_queue = infor_queue
#         self._session = requests.session()
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Host': 'www.ygdy8.net',
            }
        
    def run(self):
        while True:
            if self.page_queue.empty():
                print('page_urls is null !!!')
                return
            url = self.page_queue.get()
            self._geturls(url)
    
    def _geturls(self, url):
        response = requests.get(url, headers=self._headers)
        response.encoding = 'gbk'
        html = etree.HTML(response.text)
#         urls = html.xpath('//div[@class="co_content8"]/ul//table[@class="tbspan"]/tbody/tr/a/@href')
        urls = html.xpath('//div[@class="co_content8"]//td/b/a/@href')
        print(len(urls))
        for url in urls:
            url = 'http://www.ygdy8.net' + url
            self.infor_queue.put(url)
            
    
class consumer(threading.Thread):
    def __init__(self, page_queue, infor_queue, *args, **kargs):
        super().__init__(*args, **kargs)
        self.page_queue = page_queue
        self.infor_queue = infor_queue
        self._session = requests.session()
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Host': 'www.ygdy8.net',
            }
        
    def run(self):
        while True:
            if self.page_queue.empty():
                if self.infor_queue.empty():
                    print('over')
                    break
            url = self.infor_queue.get(block=True)
            print(url)
            self._getinfor(url)
    
    def _getinfor(self, url):
        response = requests.get(url, headers=self._headers)
        response.encoding = 'gbk'
        html = etree.HTML(response.text)
#         html = etree.parse(filename)
        chinese_name = re.findall(r'\u25ce\u8bd1\u3000\u3000\u540d\u3000(.*?)<br />', response.text)[0]
        print(chinese_name)

if __name__ == '__main__':
    page_queue = Queue(100)
    infor_urls = Queue(500)
    
    for i in range(1, 5):
        url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'.format(str(i))
        page_queue.put(url)
    
    for i in range(1):
        p = producer(page_queue, infor_urls)
        p.start()
    for i in range(1):
        c = consumer(page_queue, infor_urls)
        c.start()
    
    
    
    
    
    
    
    
    
    