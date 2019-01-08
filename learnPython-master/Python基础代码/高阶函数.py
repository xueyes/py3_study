# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/8 17:56

# 高阶函数是至少满足下列一个条件的函数:

#接受一个或多个函数作为输入
#输出一个函数

import time
def foo():
    time.sleep(3)
    print('你好啊师父')

def test(func):
    print(func)
    start_time=time.time()
    func()
    stop_time=time.time()
    print('函数运行时间%s'%(stop_time-start_time))
test(foo)
