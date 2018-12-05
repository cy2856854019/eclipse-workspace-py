'''
Created on 2018年12月5日

@author: cy
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

class QiangPiao12306():
    
    def __init__(self, from_station='上海', to_station='广州', depart_time='2018-12-06', trains='all'):
        firefoxOptions = webdriver.FirefoxOptions()
        #设置代理服务器 
        firefoxOptions.set_preference('network.proxy.type', 1) 
        firefoxOptions.set_preference('network.proxy.http','124.225.144.224')#IP为你的代理服务器地址:如‘127.0.0.0’，字符串类型 
        firefoxOptions.set_preference('network.proxy.http_port', 8060) #PORT为代理服务器端口号:如，9999，整数类型 
        self._driver = webdriver.Firefox(firefox_options=firefoxOptions)
        self._login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self._my12306_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self._homepage_url = 'https://www.12306.cn/index/index.html'
        self._from_station = from_station
        self._to_station = to_station
        self._depart_time = depart_time
        self._trains = trains
    
    def run(self):
        self._login()
    
    def _login(self):
        self._driver.get(self._login_url)
        try:
            WebDriverWait(self._driver, timeout=100).until(
                EC.url_to_be(self._my12306_url)
                )
            print('login success')
            self._Sleep()
            home_page = self._driver.find_element_by_link_text('首页')
            home_page.click()
            WebDriverWait(self._driver, timeout=30).until(
                EC.url_to_be(self._homepage_url)
                )
            print('请在60秒内输入订票信息')
            WebDriverWait(self._driver, timeout=60).until(
                EC.text_to_be_present_in_element_value((By.ID, 'train_date'), self._depart_time)
                )
            check_button = self._driver.find_element_by_link_text('查    询')
            check_button.click()
            self._order_ticket()
            time.sleep(100)
        except Exception as e:
            print('msg : ', e)
    
    def _order_ticket(self):
        try:
            self._driver.switch_to_window(self._driver.window_handles[1])
            check_btn = WebDriverWait(self._driver, timeout=30).until(
                EC.presence_of_element_located((By.XPATH, '//a[@id="query_ticket"]'))
                )
            if self._trains == 'all':
                trains = self._driver.find_elements_by_xpath('//tbody[@id="queryLeftTable"]/tr[contains(@id, "ticket")]')
                for train in trains:
                    train_text = train.find_element_by_xpath('.//td[4]').text
                    if train_text != '无':
                        order_btn = self._driver.find_element_by_link_text('预订')
                        order_btn.click()
                        WebDriverWait(self._driver, timeout=10).until(
                            EC.presence_of_element_located((By.XPATH, '//div[@class="lay-hd"]'))
                            )
                        li = self._driver.find_element_by_xpath('//label[@for="normalPassenger_0"]')
                        li.click()
                        self._Sleep()
                        submit_btn = self._driver.find_element_by_id('submitOrder_id')
                        submit_btn.click()
                        self._Sleep()
                        if WebDriverWait(self._driver,10).until(
                            EC.visibility_of_element_located((By.ID, 'content_checkticketinfo_id'))
                            ):
                            qr_submit = self._driver.find_element_by_link_text('确认')
                            qr_submit.click()
                    elif train_text == '无':
                        train = train.find_element_by_xpath('.//a[@title="点击查看停靠站信息"]').text
                        print('　%s　车次二等座已售罄' % train)
            else:
                for train in self._trains():
                    pass
        except Exception as e:
            print(e)
        
    def _Sleep(self):
        time.sleep(2)
    
    def __del__(self):
        self._driver.quit()
    
if __name__ == '__main__':
    qiangpiao = QiangPiao12306()
    qiangpiao.run()
    
    