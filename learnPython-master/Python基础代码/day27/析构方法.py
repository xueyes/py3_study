# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/14 17:00
#析构函数的调用是解释器回收机制自动执行的
class Foo:
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print("我执行啦")
f1=Foo('alex')


#del f1
del f1.name #del只有实例被删除的时候才会触发
print('------------------')

