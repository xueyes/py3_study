# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/27 14:37

class Foo:

    def get_AAA(self):
        print('get的时候运行我啊')

    def set_AAA(self, val):
        print('set的时候运行我啊',val)


    def del_AAA(self):
        print('del的时候运行我啊')


    AAA=property(get_AAA,set_AAA,del_AAA)


f1=Foo()
f1.AAA
f1.AAA='aaa'
del f1.AAA

