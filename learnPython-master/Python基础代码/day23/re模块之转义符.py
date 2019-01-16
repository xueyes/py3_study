# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/15 17:04

import re
ret = re.findall("I","I am  LIST")
print(ret)

ret = re.findall("^I","I am  LIST")
print(ret)

ret = re.findall("^I","hello I am  LIST")
print(ret)

ret = re.findall(r"I\b","hello I am  LIST") #r就是原生转义，因为\b本身在python解释器里是有定义的
print(ret)

ret = re.findall("I\\b","hello I am  LIST") #\\里面的\也是 \本身在解释器里有自己的定义
print(ret)

ret = re.findall("c\\\f","abc\ferwt")
print(ret)


ret = re.findall(r"c\\l","abc\lerwt")
print(ret)


ret = re.findall(r"ka|b","sdjkbsf") #|或者
print(ret)

ret = re.findall(r"ka|b","sdjka|bsf") #|或者
print(ret)


ret = re.findall(r"ka|bc","sdjka|bsf") #|或者
print(ret)


ret = re.findall(r"ka|bc","sdjka|bcsf") #|或者
print(ret)


ret = re.findall(r"abc+","abcabcabc")
print(ret)


ret = re.findall(r"(abc)+","abcabcabc")
print(ret)


ret = re.search("(?P<name>\w+)","abccccc").group() #返回的对象
print(ret)


ret = re.search("\d+","s34dfg5hkl4").group() #返回的对象
print(ret)



ret = re.search("(?P<name>[a-z]+)","alex36wusi34xialv33").group() #返回的对象
print(ret)

ret = re.search("[a-z]+","alex36wusi34xialv33").group() #返回的对象
print(ret)

ret = re.search("(?P<name>[a-z]+)(?P<age>\d+)","alex36wusi34xialv33").group("age") #分组
print(ret)


ret = re.match("\d+","56alex36wusi34xialv33").group() #返回的对象
print(ret)


ret = re.split(" ","hello abc def ")
print(ret)

ret = re.split("[ |]","hello abc|def ") #空格和管道符匹配
print(ret)


ret = re.split("[ab]","asdabcd")
print(ret)


ret = re.split("[ab]","abc")
print(ret)



