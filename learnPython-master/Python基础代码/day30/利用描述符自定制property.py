# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/25 16:24
class Lazypropery:
    def __init__(self,func):
        print('=====>',func)
        self.func=func
    def __get__(self, instance, owner):
        print('get')
        print(instance)
        print(owner)
        res=self.func(instance)
        return res


class Room:

    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

    @Lazypropery #area=Lazypropery(area) #语法糖


    # @property #area=property(area)
    def area(self):
            return self.width * self.length

r1=Room('cesuo',1,1)
print(r1.area)
# print(Room.__dict__)
