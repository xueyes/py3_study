# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/23 17:48


class Chinese:
    country='China'
    l = ['a','b']

    def __init__(self,name):
        self.name=name



    def play_ball(self,ball):
        print('%s正在打 %s' %(self.name,ball))
p1=Chinese('alex')
print(p1.l)

# p1.l=[1,2,3]
# print(Chinese.l)
# print(p1.__dict__)  #{'l': [1, 2, 3], 'name': 'alex'}


p1.l.append('c')
print(p1.__dict__)
print(Chinese.l)







