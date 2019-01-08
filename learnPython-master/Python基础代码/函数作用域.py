# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/8 15:23

#最重要的地方了~~  非常重要~~

# if True:
#     x = 3
#
# print(x)


# def f():
#     a = 10
# f()
# print(a)

#在python里面函数是有自己的作用域(地盘,if没有作用域

# LEGB

# x = int(2.9) #int bulit-in   系统内部调用的,最外层的作用域
#
# g_count = 0  #global 全局作用域
#
#
# def outer():
#     o_count = 1 #enclosing 嵌套作用域
#     i_count = 8
#
#     def inner():
#         i_count = 2 #local
#         print(i_count)
#
#     #print(i_count)
#     inner()
#
# outer()


# count = 10
# def outer():
#     global count  #想修改全局的话,定义global
#
#     print(count)
#     count = 20 #UnboundLocalError: local variable 'count' referenced before assignment
#     print(count)
#     # count+=1    #全局作用域不能被本地作用域修改
# outer()

# count = 0
# def outer():
#     count = 10
#     def inner():
#         nonlocal count #（enclosing作用域用nonlocal表示不是全局,从而可以进行修改。 ）
#         count = 20
#         print(count)
#     inner()
#     print(count)
# outer()

#https://www.cnblogs.com/yuanchenqi/articles/5828233.html


count = 10
def outer():
    global count
    print(count)
    count = 100 #已经加载的内存了,和全局的count没关系 （修改造成的错误的） local variable 'count' referenced before assignment
    print(count)
outer()

