# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/17 14:05

#python2中分新式类和经典类,在py3中都叫新式类

#经典类
# class Chinese:
#     '这是一个中国人的类'
#     pass
#
#
# print(Chinese)
#
# #实例到底干了什么？
#
# p1=Chinese()  #类的运行产生的是一个实例 本质就是一个return
# print(p1)
#
#
# #新式类
#
# class Chinese(object):
#     '这是一个中国人的类'
#     pass






# def test():
#     pass
#     print(test)



#直接研究

'''
属性:

1.数据属性(特征）

2.函数属性(方法)

'''

#数据属性
class Chinese:
    '这是一个中国人的类'
    dang='共产党'

# print(Chinese.dang)

#函数属性

class Chinese:
    '这是一个中国人的类'
    dang='共产党'

    def sui_di_tu_tan():
        print('朝着墙上就是一口痰')
    def cha_dui(self):  #什么样的值有意义
        print('插到了前面')



print(Chinese.dang)
Chinese.sui_di_tu_tan()
Chinese.cha_dui('元昊')


# print(dir(Chinese))  #函数属性 列表放的都是一些属性名字
# print(Chinese.__dict__) #查看类的属性字典

print(Chinese.__dict__['dang']) #本质上都是在属性字典里面找东西

Chinese.__dict__['sui_di_tu_tan']() #加括号调用内存地址
Chinese.__dict__['cha_dui'](1)

print(Chinese.__name__)
print(Chinese.__doc__)
print(Chinese.__base__)
print(Chinese.__bases__)
print(Chinese.__dict__)
print(Chinese.__module__)
print(Chinese.__class__)
