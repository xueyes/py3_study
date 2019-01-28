# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/28 17:03

#一切皆文件

#接口就是具体的函数

#abc模块 接口继承
import abc


class All_file(metaclass=abc.ABCMeta):
    @abc.abstractmethod  #抽象的方法
    def read(self):
        pass
    @abc.abstractmethod
    def write(self):
        pass


class  Disk(All_file):
    def read(self):
        print('disk read')
    def write(self):
        print('disk write')

class Cdroom(All_file):
    def read(self):
        print('cdroom read')
    def write(self):
        print('cdroom write')


class Mem(All_file):
    def read(self):
        print('mem read')
    def write(self):
        pass

#
m1=Mem()
m1.read()
m1.write()





