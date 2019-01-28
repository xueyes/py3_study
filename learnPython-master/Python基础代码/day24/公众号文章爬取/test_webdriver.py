# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/18 11:03

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(5)
driver.quit()