# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/9 16:22


import time
#装饰器的架子
def timmer(func): #func=test
    def wrapper():
        #print(func) #作用域
        start_time=time.time()
        res=func() #就是在运行test()
        #pass
        stop_time=time.time()
        print('运行时间是%s'%(stop_time-start_time))
    return wrapper


@timmer  #就相当于test=timmer(test) 语法糖
def test():
    time.sleep(3)
    print('test函数运行完毕')
# res=timmer(test) #返回的是wrapper的地址
#
# res() #执行的wrapper()

# test=timmer(test)
test()






