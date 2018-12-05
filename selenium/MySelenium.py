'''
Created on 2018年12月4日

@author: cy
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains #鼠标行为链类
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

class MySelenium(object):

    def __init__(self):
#         #设置无头的firefox 即无网页页面 chrom
#         chromeOptions = webdriver.ChromeOptions()
#         chromeOptions.set_headless()
#         chromeOptions.add_argument("--proxy-server=http://61.54.89.18:80")
#         self._driver = webdriver.Chrome(chrome_options=chromeOptions)      
        #设置无头的firefox 即无网页页面  firefox
        firefoxOptions = webdriver.FirefoxOptions()
        firefoxOptions.set_headless()
#         firefoxOptions.add_argument('--headless')#也可设置无头模式
        #设置代理服务器 
#         firefoxOptions.set_preference('network.proxy.type', 1) 
#         firefoxOptions.set_preference('network.proxy.http','140.207.155.94')#IP为你的代理服务器地址:如‘127.0.0.0’，字符串类型 
#         firefoxOptions.set_preference('network.proxy.http_port', 39354) #PORT为代理服务器端口号:如，9999，整数类型 
        self._driver = webdriver.Firefox(firefox_options=firefoxOptions)

    def open(self, url):
        self._driver.get(url)
        print(self._driver.page_source)
        with open('baidu.html', 'w') as fp:
            fp.write(self._driver.page_source)
        
    def __del__(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
#         self._driver.close()#关闭当前页面
        self._driver.quit()#退出整个浏览器 

if __name__ == '__main__':
    myselenium = MySelenium()
    myselenium.open('http://httpbin.org/ip')
    
    
    