# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/23 16:40
class Chinese:
    country = 'China'
    def __init__(self,name):
        self.name=name
    def play_ball(self,ball):
        print('%s正在打 %s' %(self.name,ball))

p1=Chinese('alex')
print(p1.__dict__)

#查看
print(p1.name)
print(p1.play_ball)
print(p1.play_ball)

#增加
p1.age=18
print(p1.__dict__)
print(p1.age)


#不要修改低等的属性字典
# p1.__dict__['sex']='male'
# print(p1.__dict__)
# print(p1.sex)


# def test(self):
#     print('我是实例的函数属性')
#
# p1.test=test
# print(p1.__dict__)
# p1.test('xxxx')


#修改
p1.age=19
print(p1.__dict__)
print(p1.age)


#删除

del p1.age
print(p1.__dict__)


