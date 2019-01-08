# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/8 16:28


# def run():
#     print('from run')
#     print('from run')
#     print('from run')
#     print('from run')
#     print('from run')
#     print('from run')
#     print('from run')
#     print('from run')
#     print('from run')
#
# run()
#
#
# def test():
#     print('from run')  #从教室的一头跑到另一头,用它来保存状态
#     yield 1
#     print('from run')
#     yield 2
#
# t = test()
# next(t)
#
# print('asdf')
# print('asdf')
# print('asdf')
# print('asdf')
# print('asdf')
#
#
#
# next(t) #执行一个next就执行一次yield 知道再次遇到下一个yield
#
# t.__next__()  #x=yield 10
# t.send('123')


#执行迭代器协议 sum for map reduce filter

#pythonic 生成器只能遍历一次


#三元表达式
# age = 10
# res=True if age > 10 else False
#
# l = ['a' for i in range(10)]
#
# g_l = ('a' for i in range(10)) #这就是生成器表达式
#

def  test():
    for i in range(4):
        yield i
t=test()

# for i in t:
#     print(i)
#
# t1=(i for i in t)
# print(list(t1))     #生成器只能遍历一次
#


t1=(i for i in t)  #相当于tl已经被next取值了
t2=(i for i in t1)  #已经next过一次了,
print(list(t1))
print(list(t2))  #生成器只能遍历一次,生成器的取值原理，执行一个next,才会执行#







