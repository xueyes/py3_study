# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/16 17:45
#类：把一类事物相同的特征和动作整合在一起
#对象就是基于类而创建的一个具体的事物(具体存在的)也是特征和动作整合在一起



#学校类：
#特征:name，addr，type
#动作:考试,招生，开除学生
#整合特征和动作


def school(name,addr,type):#为了防止一条狗也调用这个
    def init(name, addr, type):
        sch = {

            'name': 'name',
            'addr': 'addr',
            'type': 'type',
            'kao_shi': kao_shi,
            'zhao_sheng': zhao_sheng
        }

        return sch
    def kao_shi(school):
        print('%s 学校正在考试' %school['name'])
    def zhao_sheng(school):
        print('%s %s学校正在招生' % school['type'],school['name'])

    # def init(name,addr,type):
    #     sch = {
    #
    #         'name': 'name',
    #         'addr': 'addr',
    #         'type': 'type',
    #         'kao_shi': kao_shi,
    #         'zhao_sheng': zhao_sheng
    #     }
    #
    #     return sch
    return init(name,addr,type)

s1=school('old','沙河','私立')
print(s1)
print(s1['name'])
s1['zhao_sheng'](s1)

s2=school('清华','北京','公立')
print(s2)