# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/23 17:00

# class Chinese:
#     country = 'China'
#     def __init__(self,name):
#         self.name=name
#     def play_ball(self,ball):
#         print('%s正在打 %s' %(self.name,ball))
#
#
# p1=Chinese('alex')
# print(p1.country)
# p1.country='日本'
# print('类的--->',Chinese.country)
# print('实例的--->',p1.country)


# country="中国"
# class Chinese:
#
#     def __init__(self,name):
#         self.name=name
#     def play_ball(self,ball):
#         print('%s正在打 %s' %(self.name,ball))
#
#
# p1=Chinese('alex')
# print(p1.country)
# p1.country='日本'
# print('类的--->',Chinese.country)
# print('实例的--->',p1.country)





# country="中国"
# class Chinese:
#
#     def __init__(self): #只能return none
#         print('---------->?')
#         name=input('请输入用户名>>:')  #这就很low逼了,输入输出和程序黏在一起了，这里面写逻辑就ok了。
#         self.name=name
#
#     def play_ball(self,ball):
#         print('%s正在打 %s' %(self.name,ball))
#
#
# p1=Chinese()
# print(p1.name)



country="中国---------------------------"
class Chinese:
    country='中国'

    def __init__(self,name):
        self.name=name
        print('---->',country) #通过点调用才算执行,否则都是变量


    def play_ball(self,ball):
        print('%s正在打 %s' %(self.name,ball))

print(Chinese.__dict__)
print(Chinese.country)

p1=Chinese('alex') #触发init函数

# print('实例--------',p1.country)


