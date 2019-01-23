# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/18 10:57

import time
import json
from selenium import webdriver
post = {}

driver = webdriver.Chrome(executable_path="C:\\Users\\admin\AppData\Local\Programs\Python\Python35\chromedriver.exe")
driver.get('https://mp.weixin.qq.com/')
time.sleep(2)
driver.find_element_by_name('account').clear()
driver.find_element_by_name('account').snd_keys()
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys()

#在自动输完密码之后记得点一个记住我
time.sleep(5)
driver.find_element_by_xpath(".\*\\a[@class=''btn_login]").clock()

#拿手机扫二维码！
time.sleep(10)
driver.get('https://mp.weixin.qq.com/')
cookie_items = driver.get_cookies()
for cookie_items in cookie_items:
    post[cookie_items['name']] = cookie_items['value']
cookie_str = json.dumps(post)
with open('cookie.txt','w',encoding='utf-8') as f:
    f.write(cookie_str)
