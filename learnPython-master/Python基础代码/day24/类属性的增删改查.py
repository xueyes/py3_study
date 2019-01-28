# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/23 14:38

class Chinese:
    country = 'China'
    def __init__(self,name):
        self.name=name
    def play_ball(self,ball):
        print('%s正在打 %s' %(self.name,ball))

print(Chinese.country)

Chinese.country='Japan'

print(Chinese.country)
p1=Chinese('alex')
print(p1.__dict__)
print(p1.country)


#增加
Chinese.dang='共产党'

print(Chinese.dang)

print(p1.dang)


#删除
del Chinese.dang
del  Chinese.country

print(Chinese.__dict__)
# print(Chinese.country)


def eat_food(self,food):
    print('%s 正在吃%s' %(self.name,food))
    self.food=food
Chinese.eat=eat_food

print(Chinese.__dict__)
p1.eat('粑粑')