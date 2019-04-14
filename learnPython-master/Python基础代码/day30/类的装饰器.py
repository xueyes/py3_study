# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/18 11:13

#装饰器同样可以修饰类
# def deco(func):
#     print('=========')
#     return func
#
# # @deco   #test=deco(test)
# # def test():
# #     print('test 运行')
# #
# # test()
#
# @deco #Foo=deco(Foo)
#
# class Foo:
#      pass
#
# f1=Foo()
# print(f1)


#类的装饰器最基本的原理

def deco(obj):
    print('=========')
    obj.x=1
    obj.y=2
    obj.z=3
    return obj

@deco #Foo=deco(Foo)

class Foo:
     pass
print(Foo.__dict__)

f1=Foo()
print(f1)

