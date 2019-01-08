# -*- coding=utf8 -*-
__author__ = 'admin'

# a =[[1,2],3,4]
# b = a
# b[1]=123
#
# print(b)
#
# print(a)
#
#
# b2=a.copy()
# b2[2]=333333333333
#
# print(a,b,b2)

import copy

#浅拷贝=只拷贝一层

#实例类似银行联名账号
husband = ["Xiaohu",123,[15000,9000]]
wife = husband.copy()
wife[0] ="XiaoPang"
wife[1] = 345

#xiaosan = copy.copy() #浅拷贝 shallow copy


xiaosan  = copy.deepcopy(husband) #深拷贝
xiaosan[0] = "JinXin"
xiaosan[1] = 666

xiaosan[2][1] -=1999


husband[2][1] -= 3000
print(wife)

print(xiaosan)

#如果列表太大,一般都不需要浅拷贝


#深拷贝=克隆一份



