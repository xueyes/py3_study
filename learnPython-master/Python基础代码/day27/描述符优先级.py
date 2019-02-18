# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/15 10:45

class Foo:
    def __get__(self, instance, owner):
        print('===> get 方法')
    def __set__(self, instance, value):
        print('====> set 方法',instance,value)
    def __delete__(self, instance):
        print('====> delete 方法')


# f1 = Foo()
# f1.name='egon'
# print(f1.name)
# del f1.name
#自己用的时候不触发，用来代理另外一个类的属性

class Bar:
    x=Foo() #在何地？
print(Bar.x)



# Bar.x=1  #赋值的时候其实就是类属性
# print(Bar.__dict__)
# print(Bar.x)


# print(Bar.__dict__)
# b1=Bar()
#
# b1.x      #get
# b1.x=1    #set
# del b1.x  #delete
#








