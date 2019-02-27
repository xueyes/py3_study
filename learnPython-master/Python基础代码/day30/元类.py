# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/27 15:58

# class Foo:
#     pass
#
# f1=Foo()  #f1是Foo实例化的对象,那么既然python一切皆对象,那么Foo这个(类对象是从哪里来的呢

# # print(f1)
#
# print(type(f1))
# print(type(Foo))  #类的类就是type type是内建元类
#

#元来就是类的类 是类的模板

class Foo:  #Foo类是type类的一个实例

    def __init__(self):
        pass

print(Foo)
print(Foo.__dict__)

def __init__(self,name,age):
    self.name=name
    self.age=age

def test(self):
    print('====>')

FFo=type('FFo',(object,),{'x':1,'__init__':__init__, 'test':test}) #type可以生成一个类。class也可以生成一个类
print(FFo)
print(FFo.__dict__)

f1=FFo('alex',18)
print(f1.name)
f1.test()


#python中任何class定义的类其实都是tyoe类实例化的对象

