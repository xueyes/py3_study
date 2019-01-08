# -*- coding=utf8 -*-
__author__ = 'admin'

#
# def f():
#     print('ok')
#
#     return  10  #1，结束函数, 2，返回某个对象
#     print('alex')  #没有任何意义
#
#     return None #默认返回空
#
#
# #返回什么内容，又给谁呢？
# a = f()
# print(a)
# print(f())


# def add(*args): #不定长参数
#     # print(args)
#     Sum = 0
#     for i in args:  #args=(1,2,3,4,5)
#         Sum+=i
#     print(Sum)
#     return Sum
#
# a = add(1,4)
# print(a)
#


def foo():
    return 1,'123',8,[1,2,3]  #成为一个元组返回

print(foo())


#注意点：1 函数里如果没有return,会默认返回一个None
#      2 如果return多个对象,那么python会帮我们把多个对象封装成一个元组

