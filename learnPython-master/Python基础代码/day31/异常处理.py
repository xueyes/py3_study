# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/28 18:07

# age = input('>>>:')
#
# if age.isdigit():
#     int(age) #主逻辑
#
# elif age.isspace():
#     print('---->用户输入的是空格')
# elif len(age) == 0:
#     print('---->'用户输入的为空)
# else:
#     print('其他的非法输入')



# def test():
#     print('test running')
#
# choice_dic={
#     '1':test
#
# }
#
#
# while True:
#     choice=input('>>:').strip()
#      if not choice or choice not in choice_dic:
#         continue #这便是一种异常处理机制啊
#     choice_dic[choice]()
#
#
# age = input('>>>:')
#
#
# try:
#     age=input('1>>:')
#     int(age) #主逻辑
#
#     num2=input('2>>:')
#     int(num2)  #主逻辑
#
#     l=[]
#     1[10000]
#
#     dic={}
#     dic['name']
# except Exception as e:
# # except ValueError as e:
#     print(e)
#
# print(111111111111)


while True:
    try:
        age=input('1>>: ')
        int(age) #主逻辑
        break
    except Exception as e:
        print('请重新输入',e)
print('11111111111')

