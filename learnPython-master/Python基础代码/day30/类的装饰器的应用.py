# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/25 14:40

# -*- coding=utf8 -*-
__author__ = 'admin'


# @Time :2019/2/18 9:50

# import sys,os
#
# def test(x):
#     print('====>',x)
#
# test('alex')
# test(111)

class Typed:
    def __init__(self, key, expected_type):
        self.key = key
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        print('get 方法')
        # print('instamce参数【%s】' % instance)
        # print('owner参数【%s】' % owner)
        instance.__dict__[self.key] = value

    def __set__(self, instance, value):
        print('set方法')
        # print('instance参数【%s】' % instance)
        # print('value参数【%s】' % value)
        # print('=====>',self)
        if not isinstance(value, self.expected_type):
            # print('你传入的类型不是字符串，错误')
            # return
            raise TypeError('%s你传入的类型不是%s' % (self.key, self.expected_type))
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        print('delete方法')
        # print('instance参数【%s】' % instance)
        instance.__dict__.pop[self.key]

def deco(**kwargs):   ##kwargs={'name:str,'age:int}
    def wrapper(obj): #obj=People
        for key,val in kwargs.items(): #(('name',str),('age',int))
            print('===>',key,val)

            setattr(obj,key,Typed(key,val))
            #setattr(People,'name',Typed(name,str)) #People.name=Typed('name',str)
            # setattr(People,'name',str)
        return obj
    return wrapper

@deco(name=str,age=int,salary=float,gender=str)  #@wrapper ===>wrapper(People)

#装饰器可以给类增加

class People:
    name=Typed('name',int)



    def __init__(self, name, age,salary,gender,height):
        self.name = name  # 触发的是代理
        self.age = age
        self.salary = salary


# p1 = People('alex', 13, 13.3)
p1=People('213',13,13.3,'x','y')

# print(p1.__dict__)
print(People.__dict__)

# p1.name
# p1.name='egon'
# print(p1.__dict__)

# print(p1.__dict__)
#
# del p1.name
# print(p1.__dict__)

