# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/25 16:31
#
# class Hand:
#     pass
#
#
# class Foot:
#     pass
#
# class Head:
#     pass
#
# class Trunk:
#     pass
#
# class Person:
#      def __init__(self,id_num,name):
#          self.id_num=id_num
#          self.name=name
#          self.hand=Hand
#          self.foot=Foot
#          self.head=Head
#          self.trunk=Trunk
#
# p1=Person('111','alex')
# print(p1.__dict__)
#



#选课系统

class School:
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr

    def zhao_sheng(self):
        print('%s 正在招生' %self.name)


class Course:
    def __init__(self,name,price,period,school):
        self.name=name
        self.price=price
        self.period=period
        self.school=school

s1=School('oldboy','北京')
s2=School('oldboy','南京')
s3=School('oldboy','东京')

#c1=Course('Linux','10','1h',s1)


#print(c1.__dict__)

msg='''
1 老男孩 北京校区
2 老男孩 南京校区
3 老男孩 东京校区

'''

while True:
    print(msg)

    menu={
        '1':s1,
        '2':s2,
        '3':s3
}


    choice= input('选择学校>>>:')
    school_obj=menu[choice]

    name=input('《课程名》:')
    price=input('《课程费用》:')
    period=input('《课程周期》:')

    new_course=Course(name,price,period,school_obj)
    print('课程【%s】属于【%s】学校' %(new_course.name,new_course.school.name))














