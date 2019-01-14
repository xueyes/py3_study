# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/14 17:28
import sys
# print(sys.argv) #根据传输参数
#
# comand=sys.argv[1:]
# python=sys.argv[2]
#
# if comand=="post":
#     pass
#
# elif comand=="get":
#     pass


# sys.stdout.write("#")
# sys.stdout.write("#")
# sys.stdout.write("#")
# sys.stdout.write("#")

import time
for i in range(100):
    sys.stdout.write("#")
    time.sleep(0.1)
    sys.stdout.flush() #从缓冲里面刷新出来而不是等集体出来再显示







