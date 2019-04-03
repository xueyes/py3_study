#coding=utf8
_author_ = 'hashlinux'
class Typed:
    def  __get__(self, instance, owner):
        print('get 方法')
        print('instance 参数【%s】' % instance)
        print('owner c参数【%s】' % owner)

    def __set__(self, instance, value):
        print('set 方法')
        print('instance 参数【%s】' % instance)
        print('value 参数【%s】' % value)

    def __delete__(self, instance):
        print('delete 方法')
        print('instance参数【%s】' % instance)





class People:
    name=Typed()
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary



p1=People('alex',13,13.3)
p1.name
p1.name='egon'
print(p1)
print(p1.__dict__)