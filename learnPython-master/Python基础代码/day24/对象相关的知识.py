# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/17 14:46

class Chinese:
    '这是一个中国人的类'
    dang='共产党'
    # def init(name,age,gender): #这种初始化class不会翻译 初始化函数用__init__
    # def __init__(name,age,gender):
    #     dic={
    #         'name':name,
    #         'age':age,
    #         'gender':gender
    #     }
    #     return dic

    def __init__(self,name,age,gender):
        print('我是初始化函数,开始运行了')
        self.mingzi=name  #p1.mingzi=name
        self.nianji=age
        self.xingbie=gender
        print('我结束啦')
        return None #默认就是，没有意义,因此不写


    def sui_di_tu_tan():
        print('朝着墙上就是一口痰')
    def cha_dui(self):  #什么样的值有意义
        print('%s插到了前面'%self.mingzi)
    #return init(name,age,gender)  #这个就不用returun class会自动生成为return

p1=Chinese('元昊','18','female') #p1没有任何意义
print(p1.__dict__) #---->__init__(self,name,age,gender)

#p1=Chinese.__init__(p1,name,age,gender)

print(p1.__dict__['xingbie'])  #实例字典,里面不包含函数属性
print(p1.mingzi) #实际上就是到__dic__里面去找  #实例只有数据属性,没有函数属性

print(p1.dang) #dang在dic里面也没有,但是为啥会调用到？ 这就是作用域的概念，从里向外找找到chinese！

#实例属性能访问到类属性和作用域相似,冯氏理论。

print(Chinese.__dict__)
# Chinese.sui_di_tu_tan()
# Chinese.cha_dui(p1)

# p1.sui_di_tu_tan() #TypeError: sui_di_tu_tan() takes 0 positional arguments but 1 was given cla
#相当于class给传递了个p1给第一个位置参数==p1.sui_di_tu_tan(p1)

p1.cha_dui() #插队本身具有一个self参数,这不传但是依然可以运行，所以证明python传了p1给chadui

#self就是实例本身









