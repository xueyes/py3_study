# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/14 17:11


#对象必须提供一个next方法，要么方法返回迭代中的下一项，要么跑出一个异常

class Foo:
    def __init__(self,n):
        self.n=n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 13:
            raise StopIteration('终止了')
        self.n+=1
        return self.n



#
# l = list('hello')
#
# for i in l:
#     print(i)

f1 = Foo(10)
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())


for i in  f1:  #f1.__iter__() ---- f1.__iter__()
    print(i)  #obj.__next__()

#TypeError: 'Foo' object is not iterable class家inter方法
