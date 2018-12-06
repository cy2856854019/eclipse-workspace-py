'''
初始化Queue(maxsize) 创建一个先进先出的队列
qsize() 返回队列的大小
empty() 判断队列是否为空
full() 判断队列是否满了
get() 从队列中取出最后一个数据
put() 将一个数据放到队列中
'''
import threading, re, os
import requests
from urllib import request
from lxml import etree
from queue import Queue

class Producer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    
    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self._parse_page(url)
    
    def _parse_page(self, url):
        response = requests.get(url, headers=self.headers)
        html = etree.HTML(response.text)
        img_urls = html.xpath("//div[@class='page-content text-center']/div/a/img[@class='img-responsive lazy image_dta']/@data-original")
        img_names = html.xpath("//div[@class='page-content text-center']/div/a/p[@style='display: none']/text()")
#         img_urls = re.findall(r'https://ws\d+.sinaimg.cn/bmiddle/.*?\.gif', response.text)
#         img_names = re.findall(r'gif\" alt=\"(.*?)\" class', response.text)

        if len(img_urls) != len(img_names):
            print('error, ', url)
            return
        for i in range(len(img_urls)):
            self.img_queue.put((img_urls[i], img_names[i]))
                                                              
class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    
    def run(self):
        while True:
            if self.img_queue.empty():
                if self.page_queue.empty():
                    return
            img = self.img_queue.get(block=True)
            url,filename = img
            print(url, filename)
            request.urlretrieve(url,'images/'+filename)
            print(filename+'  下载完成！')

def main():
    page_queue = Queue(100)
    img_queue = Queue(500)
    for x in range(1,20):
        url = "http://www.doutula.com/photo/list/?page=%d" % x
        page_queue.put(url)

    for x in range(5):
        t = Producer(page_queue,img_queue)
        t.start()

    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    main()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        