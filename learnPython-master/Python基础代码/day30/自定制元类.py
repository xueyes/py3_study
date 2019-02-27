# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/27 17:06

# class Foo(metaclass=type): #type('Foo',(object,),{})
#     def __init__(self,name):
#         self.name=name
#
#  f1=Foo('name')
#


class MyType(type):
    def __init__(self,a,b,c):
        print('元类的构造函数执行')
        print(a)
        print(b)
        print(c)

    def __call__(self, *args, **kwargs):
        # print('======>')
        # print(self)
        # print(*args,**kwargs)
        obj=object.__new__(self) #object__new__(Foo)  --> f1
        # self.__init__(obj,*args,**kwargs)  #调用Foo.__init__()
        return obj

class Foo(metaclass=MyType): #Foo=MyType(Foo，'Foo',(object,{})-->__init__
    def __init__(self,name):
        self.name=name  #f1.name=name

# f1=Foo('name')
# print(Foo)
f1=Foo('alex')
print(f1)
print(f1.__dict__)

#Foo()  #其实就是调用对象里面封装的call方法
