'''
Created on 2018年12月3日

@author: cy
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from lxml import etree
import time, threading
from queue import Queue

class LagouSpdier(threading.Thread):
    
    def __init__(self, detail_queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        firefoxOptions = webdriver.FirefoxOptions()
#         firefoxOptions.add_argument('--headless')
        #设置代理服务器 
        firefoxOptions.set_preference('network.proxy.type', 1) 
        firefoxOptions.set_preference('network.proxy.http','124.225.144.224')#IP为你的代理服务器地址:如‘127.0.0.0’，字符串类型 
        firefoxOptions.set_preference('network.proxy.http_port', 8060) #PORT为代理服务器端口号:如，9999，整数类型 
        self._driver = webdriver.Firefox(firefox_options=firefoxOptions)
        self._detail_queue = detail_queue
    
    def run(self):
        url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self._driver.get(url)
        while True:
            try:
                next_button = WebDriverWait(self._driver, timeout=5).until(
                    EC.presence_of_element_located((By.XPATH, '//span[contains(@class, "pager_next")]'))
                    )
                self.parse_list_page(self._driver.page_source)
                
                if 'pager_next pager_next_disabled' in next_button.get_attribute('class'):
                    break
                else:
                    next_button.click()
            except Exception as e:
                print(e)
            time.sleep(3)
            
    
    def parse_list_page(self, page_soure):
        html = etree.HTML(page_soure)
        detail_urls = html.xpath('//a[@class="position_link"]/@href')
        for detail_url in detail_urls:
            self._detail_queue.put(detail_url)
            time.sleep(3)
        
    def __del__(self):
        self._driver.quit()

class Parse(threading.Thread):
    
    def __init__(self, detail_queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        firefoxOptions = webdriver.FirefoxOptions()
#         firefoxOptions.add_argument('--headless')
        #设置代理服务器 
        firefoxOptions.set_preference('network.proxy.type', 1) 
        firefoxOptions.set_preference('network.proxy.http','180.104.107.46')#IP为你的代理服务器地址:如‘127.0.0.0’，字符串类型 
        firefoxOptions.set_preference('network.proxy.http_port', 45700) #PORT为代理服务器端口号:如，9999，整数类型 
        self._driver = webdriver.Firefox(firefox_options=firefoxOptions)
        self._detail_queue = detail_queue
        
    def run(self):
        while True:
            if self._detail_queue.empty():
                time.sleep(3)
            detail_url = self._detail_queue.get()
            self._driver.get(detail_url)
            try:
                WebDriverWait(self._driver, timeout=5).until(
                    EC.presence_of_element_located((By.XPATH, '//span[@class="advantage"]'))
                    )
                self.parse_detail_page(self._driver.page_source)
            except Exception as e:
                print(detail_url, e)
            time.sleep(3)
        
    def parse_detail_page(self, page_source):
        html = etree.HTML(page_source)
        job_name = html.xpath('//div[@class="job-name"]/@title')
        print(job_name)
    
    def __del__(self):
        self._driver.quit()
    
if __name__ == '__main__':
    detail_queue = Queue(100)
    
    lagouspider = LagouSpdier(detail_queue)
    lagouspider.start()
    
    for i in range(5):
        parse = Parse(detail_queue)
        parse.start()
        parse.join()
    
    lagouspider.join()
