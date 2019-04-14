# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/25 16:24
class Lazyproperty:
    def __init__(self,func):
        # print('=====>',func)
        self.func=func
    def __get__(self, instance, owner):  #描述符代理别人的
        print('get')
        print(instance)
        print(owner)
        if instance is None:
            return self
        res=self.func(instance)
        setattr(instance,self.func.__name__,res) #操作字典
        return res

    def __set__(self, instance, value):  #数据描述符高于 导致延迟效果失效
        pass


class Room:

    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

    @Lazyproperty #area=Lazypropery(area) #语法糖


    #@property #area=property(area)
    def area(self):

            return self.width * self.length

    @property  #test=property(test)
    def area1(self):
        return self.width * self.length



r1=Room('cesuo',1,1)

#实例调用
# print(r1.area)
# print(Room.__dict__)

#类调用
# print(Room.area)
#
# # print(r1.test)
# print(Room.test)

# print(r1.area1)
# print(r1.area1)
# print(r1.area1)
# print(r1.area1)


print(r1.area)
print(r1.__dict__)

print(r1.area)
print(r1.area)
print(r1.area)
print(r1.area)
print(r1.area)
print(r1.area)
print(r1.area)