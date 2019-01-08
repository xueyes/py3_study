# -*- coding=utf8 -*-
__author__ = 'admin'






# def print_info(name,age):
#     print('Name: %s' %name)
#     print('age: %d' %age)  #%d 数字
#
#
# print_info('xiaohu',38) #必须参数
#
# print_info(age=39,name='xiaohu') #2：关键字参数
#




#默认参数 在形参里面去加

# def print_info(name,age,sex='male'):  #大多数情况的话,就sex='male' 默认参数sex跟在其他参数后面
#     print('Name: %s' %name)
#     print('Age: %d' %age)  #%d 数字
#     print('Sex: %s' %sex)
#
# # print_info('xiaohu',40,'male')
# # print_info('jinxin',42,'male')
# # print_info('wuchao',43,'male')
# #
# #
# print_info('xiaohu',40)
# print_info('jinxin',42)
# print_info('wuchao',43)
# print_info('chunhua',18,'female') #性别特殊的情况就直接特殊传参


# def add(x,y):
#     print(x+y)
#
# add(1,2)  #太low了

#高大上的加法器
#
# def add(*args): #不定长参数
#     print(args)
#     sum = 0
#     for i in args:  #args=(1,2,3,4,5)
#         sum+=i
#     print(sum)
#
# add(1,2,3,6,7,9)



# def print_info(name, age, sex, job, hoby):#大多数情况的话,就sex='male' 默认参数sex跟在其他参数后面
def print_info(sex='male',*args,**kwargs):
    # print(sex)
    print(args)
    # print(args)  #('alex', 18, 'male')
    # print(kwargs)  #{'hoby': 'girls', 'height': 188, 'job': 'IT'}
    for i in kwargs:
        print('%s:%s'%(i,kwargs[i]))

    # print('Name: %s' %name)
    # print('Age: %d' %age)  #%d 数字
    # print('Sex: %s' %sex)
    # print('Job：%s' %job)
    # print('Hoby: %s' %hoby)

# print_info('alex',18,'male',job='IT',hoby='girls',height=188)

#(*args) 不定长的参数放在元组里 （**kargs）这个就是键值对的形式


# def f(*args,**kwargs):
#     pass
#
# f(1,2,'23'[123,4],name='alvin',age=24)
#
# *** 关于不定长参数的位置 *args放在左边,**kwargs 放在右边
#如果有默认参数,放最左边。  关键参数的优先级最高,所以最左边.
#def func(name,age=22,*args,**kwargs):



# print_info('alex',18,'male',job='IT',hoby='girls',height=188)

print_info()
print_info('female',1,2,34)
print_info('ttt',2,34,'female',name='hello')  #第一个默认的










