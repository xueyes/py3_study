# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/14 17:06

class Foo:
    def __call__(self, *args, **kwargs):
        print("实例执行啦 obj()")
    pass

f1=Foo()

f1()

#对象后面加括号，触发执行，是调用类下的call方法执行。





