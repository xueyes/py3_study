
# -*- coding=utf8 -*-
__author__ = 'admin'


# p = [(),]
#
#     if:
#
#
#     elif:
#
#
#     else:


# def show_shopping_car():...
#
#
#
# show_shopping_car()
#
# if 1:
#     show_shopping_car()
# else:
#     show_shopping_car()
#


#账单记录日志



# def logger(log_text):
#     f = open('log.txt', 'a')
#     f.write("2016-08-25 15:24 %s" % log_text)  #有30万行需要改时间,打到屏幕上
#     f.close()
    #print(log_text)



#函数 ！= function()
#计算机函数 == subroutine 子程序， procedures 过程
#作用:
    # 1.减少了重复代码
    # 2.方便修改,更易扩展
    # 3.保持代码一致性


print("----function 1")

# f = open('log.txt','a')
# f.write("2016-08-25 15:24 exec function 1")  #有30万行需要改时间,打到屏幕上
# f.close()
# print("2016-08-25 15:24 exec function 1")
# logger("2016-08-25 15:24 exec function 1)


print("----function 2")

# f = open('log.txt','a')
# f.write("exec function 2")
# f.close()
# logger("2016-08-25 15:24 exec function 2)


print("----function 3")
# f = open('log.txt','a')
# f.write("exec function 3")
# f.close()
# logger("2016-08-25 15:24 exec function 3)


# def f(index):
#     print('function  %s' %index)
#
#
# f(3) #调用一定加括号
# f(5)



# def add(x,y):  #形参 按顺序对应
#     print(x)
#     print(y)
#     print(x+y)
#
# add(10,5) #实参
# # add(5,8)
# #形参接受实参

import time

# print(time_current)

def logger(n):
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)

    with open('日志记录', 'a') as f:
        f.write('%s end action%s\n' %(time_current,n))  #格式化输出 %s占位符 两个变量组成一个元组,填充字符串。



def action1(n):
    # print('starting action1......')

    # with open('日志记录','a') as f:
    #     f.write('end action%s\n' %n)
    logger(n)

def action2(n):
    # print('starting action2......')
    # with open('日志记录','a') as f:
    #     f.write('end action%s\n' %n)
    logger(n)


def action3(n):
        # print('starting action3.....')
        # with open('日志记录', 'a') as f:
        #     f.write('end action%s\n' % n)
        logger(n)

#四个函数相当于放置在内存里了，传了实参才会生效

action1(11)
action2(22)
action3(33)






