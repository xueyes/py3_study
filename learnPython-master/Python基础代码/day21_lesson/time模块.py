# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/14 14:52
import time

#三种时间的表达式
#时间戳

# print(time.time()) #1547449343.702 秒数1970年一月一日到现在经历的秒数  1970年是unix诞生的时间,漂移时间
#
#
# #结构化时间
# print(time.localtime(time.time())) #东八区
# print(time.localtime(1847449343))
# t=time.localtime()
# print(t.tm_year)
# print(t.tm_wday)

#
# print(time.gmtime()) #世界标准时间utc


#字符串时间
#'2016-12-13'



#结构化时间转换为时间戳


# print(time.mktime(time.localtime()))

#将结构化时间转换成字符串时间
# print(time.strftime("%Y-%m-%d %X",time.localtime()))


#将字符串时间转换成结构化时间

# print(time.strptime("2019:01:14:15:24:38","%Y:%m:%d:%X"))

# print(time.asctime())
# print(time.ctime())


import datetime
print(datetime.datetime.now())

