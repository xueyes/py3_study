# import requests
#
#
# def now():
#     print('this is Python')
#
#
# f = now
# f()
# print(now.__name__)


# l = [1,2,3]
# l.__iter__()  #iter(1) 迭代器

#装饰器：本质就是函数，为其他函数添加附加功能

#原则：

#1 不修改被修饰函数的源代码
#2 不修改被修饰函数的调用方式

# import time
# def cal(l):
#     start_time=time.time()
#     res = 0
#     for i in l:
#         time.sleep(0.01)
#
#         res+=i
#     stop_time = time.time()
#     print('函数的运行时间是%s' %(stop_time-start_time))
#     return res
#
#
# print(cal(range(100)))
#
#
#
# def index():
#     pass
#
#
#
# def home():
#     pass

#开放封闭原则:不轻易修改程序源代码

# 
# index()
# home()
#装饰器的知识储备

#装饰器=高阶函数+函数嵌套+闭包


# import time
# def cal(l):
#     start_time=time.time()
#     res = 0
#     for i in l:
#         time.sleep(0.1)
#
#         res+=i
#     # stop_time = time.time()
#     # print('函数的运行时间是%s' %(stop_time-start_time))
#     return res
#
#
# print(cal(range(20)))



import time
def timmer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time = time.time()
        print('函数运行的时间%s' %(stop_time-stop_time))
        return res
    return wrapper

@timmer
def cal(l):
    res = 0
    for i in l:
        time.sleep(0.1)
        res+=i
    return res
res=(cal(range(20)))
print(res)
