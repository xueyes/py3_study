# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/27 14:23

class ClassMethod:
    def __init__(self,func):
        self.func=func



    def __get__(self, instance, owner):
        def feedback(*args,**kwargs):
            print('这里可以加功能啊')
            return self.func(owner,*args,**kwargs)
        return feedback
class People:
    name='xuehui'
    @classmethod  #say_hi=ClassMethod(say_hi)
    def say_hi(cls,msg):
        print('你好啊,帅哥 %s  %s' %(cls.name,msg))

People.say_hi('你是那偷心的贼')

# p1=People()
# p1.say_hi('你是那偷心的贼')
