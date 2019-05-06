#coding=utf8
_author_ = 'hashlinux'
#http://www.cnblogs.com/sunkai1993/articles/6160149.html
#三元运算
# a = 1
# result = "xiaoming" if a == 1 else "xiaogang"
# print(result)

#lambda 表达式
# def func(arg):
#     return  arg + 1
# func(2)
# print(func(2))

# func = lambda *args :print(args)
# print(func(1,2,3))

#map
# li = [1,2,3,4,5]
#
# def func(s):
#     return s + 1
# ret = map(func,li) #input-->map--->putput
# print(next(ret))
# print(list(ret))

# print(list(map(lambda li : li + 1 , li ))) #高级版本



#filter 筛选 过滤

li = [22,33,44,55,66]

# def func(s):
#     if s > 33:
#         return s
# ret = filter(func,li)
# print(list(ret))
#
#
# print(list(filter(lambda s : s > 33,li))) #高级别
#

#reduce  #所有元素累计操作
from  functools import reduce

# li = [1,2,3,4]
# li = ["a","l","e","x"]
# def func(a,b):
#     return a+b
# ret = reduce(func,li)
# print(ret)


# li = [1,2,3,4]
# print(reduce(lambda a,b:a+b,li))

# li=range(1,100)
# # print((lambda a,b:a*b,li))

def multi99():
    result = ''
    for i in range(1, 10):
        for j in range(1, i + 1):
            separator = '\n' if j == i else '\t'
            result += '%d * %d = %-2d' % (j, i, i * j)
            result += separator
    return result

print(multi99())

print(''.join(['%d * %d = %-2d'%(y,x,x*y)+(lambda x,y:'\n' if x == y else '\t')(x,y) for x in range(1,10) for y in range(1,x+1)]))

