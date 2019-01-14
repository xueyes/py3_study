# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/14 15:44
import random

# ret = random.random()
# ret = random.random()
#
# print(random.randint(1,3))
# print(random.randrange(1,3))
# print(random.choice([11,22,33,44,55]))
# print(random.sample([11,22,33,44,55],2))
# print(random.uniform(1,3))
#
#
# item=[1,3,5,7,9]
# random.shuffle(item)
# print(item)

def v_code():

    ret = ""

    for i in range(5):
        num = random.randint(0,9)
        alf= chr(random.randint(65,122)) #数字对应的字母
        s=str(random.choice([num,alf]))  #choice随机选
        ret+=s
    return ret

print(v_code())




#
# 顶级可行的代码
# print('')
# 只要有缩进的就是局部作用于



def test():
    pass

if __name__ == '__main__':
    while

