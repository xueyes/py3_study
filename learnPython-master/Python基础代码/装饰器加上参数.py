# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/9 16:43
import time
#装饰器的架子
def timmer(func): #func=test
    # def wrapper(name,age,gender): #以下类似都用*args，**kwargs同写
    def wrapper(*args,**kwargs):
        #print(func) #作用域
        start_time=time.time()
        res=func(*args,**kwargs) #就是在运行test()
        #pass
        stop_time=time.time()
        print('运行时间是%s'%(stop_time-start_time))
        return res
    return wrapper


@timmer  #就相当于test=timmer(test) 语法糖
def test(name,age):
    time.sleep(1)
    print('test函数运行完毕,名字是【%s】年龄是【%s】'%(name,age))
    return '这是test的返回值'

res=test('linhaifeng',18)  #就是在运行wrapper
# print(res)


@timmer
def test1(name,age,gender):
    time.sleep(1)
    print('test1函数运行完毕,名字是【%s】年龄是【%s】性别是【%s】'%(name,age,gender))
    return '这是test1的返回值'

test1('alex',18,'male')


#a,b,c={1,2,3}  解压序列 一一对应的关系

#l = [1,2,3,4,5,6,7,8]
#a,*_,d = l


#京东后端就是一个个的功能

#都装上一个验证功能

def index():
    pass

def home():
    pass


def shooping_car():
    pass


def order():

    pass




