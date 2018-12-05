'''
Created on 2018年12月4日

@author: cy
'''
import requests, time, random

session = requests.session()
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python',
    }
headers = {
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Cookie' : 'JSESSIONID=ABAAABAABEEAAJAA004A2B0C856C3574CD8DD40EEDACADF; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543461874; _ga=GA1.2.1103149589.1543461874; user_trace_token=20181129112433-4a9c8346-f386-11e8-8489-525400f775ce; LGUID=20181129112433-4a9c8682-f386-11e8-8489-525400f775ce; index_location_city=%E4%B8%8A%E6%B5%B7; _gid=GA1.2.1817636720.1543894755; LGSID=20181204113915-2c31c75b-f776-11e8-89e4-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20181204113923-30c9441c-f776-11e8-89e4-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1543894763; TG-TRACK-CODE=search_code; SEARCH_ID=c391f95bd8fb4688a0a1620e86db5862',
    }
proxies = ['182.150.35.89:8080', '183.129.244.16:12471', '220.164.126.62:41146', '115.223.251.105:9000', '119.57.105.25:53281', '220.164.126.62:41146']
proxy = {
    'http': random.choice(proxies),
}
for x in range(1, 10):
    data['pn'] = x
    response = session.post(url, headers=headers, data=data, proxies=proxy)
#     response.encoding = 'utf-8'
#     print(response.text)
    print(type(response))
    print(type(response.json()))
    time.sleep(3)
