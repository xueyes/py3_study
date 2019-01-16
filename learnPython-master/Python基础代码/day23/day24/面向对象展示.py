# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/16 18:15

class Dog:  #class再不用return一个结果,本质上在执行初始化函数返回一个值
    def __init__(self,name,gender,type):
        self.name=name
        self.gender=gender
        self.type=type


    def bark(self):
        print('一条名字为[%s]的[%s],狂吠不止'%(self.name,self.type))


    def yao_ren(self):
        print('[%s]正在咬人' % (self.name))


    def chi_shi(self):
        print('[%s],正在吃屎' % (self.type))



dog1=Dog('alex','femal','京巴')
print(dog1.__dict__) #实际上再返回字典
dog2=Dog('wupeiqi','female','腊肠')
dog3=Dog('yuanhao','female','藏獒')


dog1.bark()
dog2.yao_ren()
dog3.chi_shi()