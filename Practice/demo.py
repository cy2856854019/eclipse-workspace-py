'''
Created on 2018年11月29日

@author: cy
'''
# from urllib import parse
# data = {'name':'爬虫', 'greet':'hello world', 'age':100}
# qs = parse.urlencode(data)
# print(qs)
# print(parse.parse_qs(qs))

# from urllib import parse
# url = 'http://www.baidu.com/s;hello?username=zhiliao#1'
# result = parse.urlparse(url)
# #result = parse.urlsplit(url)
# print(result)
# print('scheme:', result.scheme)
# print('netloc:', result.netloc)
# print('path:', result.path)
# print('query:', result.query)
# print('fragment:', result.fragment)

# from urllib import request
# 
# url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# headers = {
#     'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
#     
#     }
# req = request.Request(url, headers=headers)
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# from urllib import request, parse
# 
# headers = {
#     'Host': 'www.lagou.com',
#     'Origin': 'https://www.lagou.com',
#     'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
#     }
# data = {
#     'first': 'true',
#     'pn': 1,
#     'kd': 'python',
#     }
# url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
# req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# from urllib import request
# url = 'http://httpbin.org/ip'
# handler = request.ProxyHandler({'http':'180.164.24.165:53281'})
# opener = request.build_opener(handler)
# #req = request.Request(url)#如果只有url参数 没有data headers等 可直接将url传给下面的函数
# response = opener.open(url)
# print(response.read().decode('utf-8'))

# from urllib import request
# 
# # request.urlretrieve('http://www.renren.com/880151247/profile', 'renren.html')
# headers = {
#     'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
#     'Cookie': "anonymid=jp26kvq1hjzykf; depovince=SH; jebecookies=342ce692-8729-4997-bd47-9b96c3948dad|||||; _r01_=1; ick_login=bb29c8e0-b374-45c6-903f-d8aa4da2d292; jebe_key=3a92c938-5510-41db-a0e4-b016d8d3d285%7Ccfcd208495d565ef66e7dff9f98764da%7C1543470637443%7C0; _de=B14079CDB54B20DF6B33C40BF6017782; p=c9b0db36ece46ee898bb42a5ef6fd3692; first_login_flag=1; ln_uact=15988416341; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=38b12078d2855e7620b30e945f414d0d2; societyguester=38b12078d2855e7620b30e945f414d0d2; id=965273582; xnsid=a1fa900b; loginfrom=syshome",
#     }
# url = 'http://www.renren.com/880151247/profile'
# req = request.Request(url, headers=headers)
# response = request.urlopen(req)
# with open('renren.html', 'w') as fp:
#     fp.write(response.read().decode('utf-8'))

# from urllib import request
# from http.cookiejar import MozillaCookieJar
#  
# cookiejar = MozillaCookieJar('cookie.txt')
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)
# opener.open('http://httpbin.org/cookies/set/course/abc')
# cookiejar.save(ignore_discard=True, ignore_expires=True)

# from urllib import request, parse
# from http.cookiejar import MozillaCookieJar
# 
# def get_opener():
#     mozillacookiejar = MozillaCookieJar()
#     handler = request.HTTPCookieProcessor(mozillacookiejar)
#     opener = request.build_opener(handler)
#     return opener
# 
# def login(opener):
#     headers = {
#     'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
#     'Host' : "www.renren.com",
#     'Referer' : "http://www.renren.com/SysHome.do",
#     }
#     url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20181041435679'
#     data = {"email": "15988416341", "password": "0.123university"}
#     data = parse.urlencode(data).encode('utf-8')
#     req = request.Request(url, headers=headers, data=data)
#     opener.open(req)
#     return opener
# 
# def self_page(opener):
#     url = 'http://www.renren.com/880151247/profile'
#     response = opener.open(url)
#     with open('renren.html', 'w') as fp:
#         fp.write(response.read().decode('utf-8'))
# 
# opener = get_opener()
# opener = login(opener)
# self_page(opener)

import requests
proxy = {
    'http':'119.254.94.95:56942',
    }
response = requests.get('http://httpbin.org/ip', proxies=proxy)
print(response.text)
    
    
