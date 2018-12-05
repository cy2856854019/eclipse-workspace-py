'''
Created on 2018年12月3日

@author: cy
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from lxml import etree
import time

class LagouSpdier():
    
    def __init__(self):
        firefoxOptions = webdriver.FirefoxOptions()
        firefoxOptions.add_argument('--headless')
        #设置代理服务器 
        firefoxOptions.set_preference('network.proxy.type', 1) 
        firefoxOptions.set_preference('network.proxy.http','139.224.233.9')#IP为你的代理服务器地址:如‘127.0.0.0’，字符串类型 
        firefoxOptions.set_preference('network.proxy.http_port', 80) #PORT为代理服务器端口号:如，9999，整数类型 
        self._driver = webdriver.Firefox(firefox_options=firefoxOptions)
    
    def run(self):
        url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self._driver.get(url)
        while True:
            try:
                next_button = WebDriverWait(self._driver, timeout=5).until(
                    EC.presence_of_element_located((By.XPATH, '//span[contains(@class, "pager_next")]'))
                    )
#                 with open('1.html', 'w') as fp:
#                     fp.write(self._driver.page_source)
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
            self._driver.execute_script('window.open("%s")' % detail_url)
            self._driver.switch_to_window(self._driver.window_handles[1])
            try:
                WebDriverWait(self._driver, timeout=5).until(
                    EC.presence_of_element_located((By.XPATH, '//span[@class="advantage"]'))
                    )
                self.parse_detail_page(self._driver.page_source)
            except Exception as e:
                print(detail_url, e)
            time.sleep(3)
    
    def parse_detail_page(self, page_source):
#         with open('1.html', 'w') as fp:
#             fp.write(page_source)
        html = etree.HTML(page_source)
        job_name = html.xpath('//div[@class="job-name"]/@title')
        print(job_name)
        self._driver.close()
        self._driver.switch_to_window(self._driver.window_handles[0])
    
    def __del__(self):
        self._driver.quit()
    
if __name__ == '__main__':
    lagouspider = LagouSpdier()
    lagouspider.run()


