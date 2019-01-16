# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/15 15:48

import re
#正则是一种小型的,高度专业化的编程语言。

#371481198506143635
#110481198506143635


#^110......1990+* #北京所有1990年后的人

# t = re.findall('\d+',"alex23json345weni678")
# print(t)
#
# ret=re.findall('a..in','helloalvin')
# print(ret)  #['alvin']

#.叫做通配符(除了\n所有的都可以匹配)
#重复符号 *（0，+00） +（1，+00） ?(0,1) {}  {0，}==*  {1，}==+ {0,1}== ？ {6}={1,6}万能的

# d = re.findall("^d*","ddddddjfjhlhhhdddkhkjhkjddd")
# print(d)

# ale=re.findall("www[oldboy,baidu]","wwwbaidu")
# print(ale)

print(re.findall("x[yz]","xyuuuu"))
print(re.findall("x[yz]","xyuuxzuu"))
print(re.findall("x[yz]p","xypuuxzpuu"))  #[]或的作用


print(re.findall("q[a*z]","ksadfkqaa"))  #['qa']
print(re.findall("q[a-z]","quo"))  #['qu']
print(re.findall("q[a-z]*","quo"))  #['quo']


print(re.findall("q[a-z]*","quogkkjkj9"))  #['quogkkjkj']

print(re.findall("q[0-9]*","quogkkjkj9"))  #['q']


print(re.findall("q[0-9]*","q88uogkkjkj9"))  #['q88']


print(re.findall("q[^a-z]","qz"))  #[]

#"12+(34*6+2-5*(2-1))"
# print(eval("12+(34*6+2-5*(2-1))"))

js=re.findall("\([^()]*\)","12+(34*6+2-5*(2-1))") #字符集特殊的 - ^ \
print(js)

#\ 是最牛逼的,让有意义的变为没意义 \d == 0-9任何数字

sz= re.findall("\d","12+(34*6+2-5*(2-1))")
print(sz)


print(re.findall("\D+","hello world"))
print(re.findall("S+","hello world"))

print(re.findall("www.baidu.","www/baidu.com"))
print(re.findall("www\*baidu.","www*baidu.com"))















