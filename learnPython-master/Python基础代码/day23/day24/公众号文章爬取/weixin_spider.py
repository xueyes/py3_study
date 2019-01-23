# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/18 11:27
'''
给予该公号的id

'''

import json
import requests
import re
gzlist = {'sxcht777'}

url = 'https://mp.weixin.qq.com'
header = {
    "HOST":"mp.weixin.qq.com"
    "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}
cookie= '{ua_id=g2ElNzy9k9Ni8s5tAAAAAGWot8Pz7uD4oNMCSZfBQ3Q=; mm_lang=zh_CN; pgv_pvi=5840266240; pgv_si=s3202955264; UM_distinctid=1685e9593d83bf-09ff96653c006e-4446062d-1fa400-1685e9593d990a; uuid=8b806cb73b07932c421b850065e054a3; ticket=faf981a6934cefe557d2de5a2d5880f095eba4b7; ticket_id=gh_f5b44f7d1cd3; cert=KMY_9MWs8dBodE33bOD5R18sZc0Vbx0K; noticeLoginFlag=1; data_bizuin=3248864923; bizuin=3269713796; data_ticket=xJeEsq5QLII1NL4SfuRV0wnlmxFDLRatJQTTwFlGM0pHhK6wNeCLDuEIVZ3Yozdj; slave_sid=aHU1X05tUldnaTJObXl6NERFU3JYbWVnam81VW5MYnVWRVMwRVFIdGdmS2E5R2pFbHZRMEdGa2h4aGZ5d2pJWjRFSEZJaVpORTRsUFVhRmRCb21iczg4M2J2ZjVxMkNReFFQenM3MUFEMEFIUDlHMTNFTmNHRTJ6eDFtUURpeUNkVFVUWVVyQjY5ekw2UXFP; slave_user=gh_f5b44f7d1cd3; xid=c1e9dd31220abf703e419273edb6a9ef; openid2ticket_om76lwdP0d-XFP2Rrbn4PkqzRkQo=nbkjcA2QBW34g49m0FUDUBsDvnE8DXG9WsPYRBx2GpU=; CNZZDATA1272425418=1762922439-1547771824-https%253A%252F%252Fwww.baidu.com%252F%7C1547777224; rewardsn=; wxtokenkey=777; CNZZDATA1272960370=519626773-1547774922-https%253A%252F%252Fwww.baidu.com%252F%7C1547780322}'
cookies = json.loads(cookie)
response = requests.get(url=url,cookies=cookie)
token = re.findall(r'token={\d+}',str(response.url))[0]
print(token)
for query in gzlist:
    query_id = {
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'begin': '0',
        'count': '5',
        'query': 'query',


    }
    search_url ='https://mp.weixin.qq.com/cgi-bin/serchbiz?'
    search_response = requests.get(search_url,cookies=cookies,headers=header,params=query_id)
    tmp_url = search_response.json().get('list')[0]
    print(lists)
    fakeid = lists.get('fakeid')
    query_id_data={
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'begin': '0',
        'count': '5',
        'query':'',
        'fakeid':fakeid,
        'type':'9'
    }
    appmsg_url='https://mp.weixin.qq.com/cgi-bin/appmsg?'
    appmsg_response=requests.get(appmsg_url,cookies=cookies,headers=header,params=query_id_data)
    tmp_url2 = appmsg_response.url
    print(tmp_url2)
    max_num= appmsg_response.json().get('app_msg_cnt') #发布文章总数
    article_lists=appmsg_response.json().get('app_msg_list') #发布的文章list
    print(article_lists)

