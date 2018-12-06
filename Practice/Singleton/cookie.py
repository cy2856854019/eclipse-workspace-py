'''
使用cookielib库和HTTPCookieProcessor模拟登陆
'''

import requests

headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Host' : "www.renren.com",
    'Referer' : "http://www.renren.com/SysHome.do",
    }
login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20181041330677'

class Cookie():    
    def get_cookie(self, response):
        Type = type(response)
        if Type == requests.models.Response:
            cookie = response.cookies.get_dict()
            return cookie
    
    def login2_renren(self):
        data = {
            "email": "15988416341", 
            "password": "0.123university"
            }
        session = requests.session()
        response = session.post(login_url, headers=headers, data=data)

        return response

mycookie = Cookie()
response = mycookie.login2_renren()
cookies =  mycookie.get_cookie(response)








