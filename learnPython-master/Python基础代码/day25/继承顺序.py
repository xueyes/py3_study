# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/29 13:48

#深度优先

class A:
    def test(self):
        print('A')


class B(A):
    def test(self):
        print('B')

class C(A):
    def test(self):
        print('C')

class D(B):
    def test(self):
        print('D')

class E(C):
    def test(self):
        print('E')


class F(D,E):
    # def test(self):
    #     print('F')
    pass

f1=F()
# f1.test()

print(F.__mro__)






