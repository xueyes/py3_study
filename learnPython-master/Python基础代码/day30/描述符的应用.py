# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/18 9:50

# import sys,os
# 
# def test(x):
#     print('====>',x)
# 
# test('alex')
# test(111)

class Typed:
    def __init__(self,key,expected_type):
        self.key=key
        self.expected_type=expected_type

    def __get__(self, instance, owner):
        print('get 方法')
        # print('instamce参数【%s】' % instance)
        # print('owner参数【%s】' % owner)
        instance.__dict__[self.key]=value

    def __set__(self, instance, value):
        print('set方法')
        # print('instance参数【%s】' % instance)
        # print('value参数【%s】' % value)
        # print('=====>',self)
        if not isinstance(value,self.expected_type):
            # print('你传入的类型不是字符串，错误')
            # return
            raise TypeError('%s你传入的类型不是%s'%(self.key,self.expected_type))
        instance.__dict__[self.key]=value

    def __delete__(self, instance):
        print('delete方法')
        # print('instance参数【%s】' % instance)
        instance.__dict__.pop[self.key]



class People:
    name=Typed('name',str)
    age=Typed('age',int)
    def __init__(self,name,age,salary):
        self.name=name  #触发的是代理
        self.age=age
        self.salary=salary
        

p1=People('alex',13,13.3)
# p1=People('213',13,13.3)
# print(p1.__dict__)

# p1.name
# p1.name='egon'
# print(p1.__dict__)

# print(p1.__dict__)
#
# del p1.name
# print(p1.__dict__)

