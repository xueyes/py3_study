# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/14 16:56
import os

# print(os.getcwd())
# os.chdir("..")
# print(os.getcwd())
# print(os.makedirs('dir1/dir2'))
# os.removedirs("dir1/dir2") #有内容只删除空的

# print(os.listdir())
#
# print(os.stat("sss.py"))
#
# print(os.system("dir"))

# print(os.path.split(r"F:\py3_study\learnPython-master\Python基础代码\day22\sss.py"))
# print(os.path.dirname(r"F:\py3_study\learnPython-master\Python基础代码\day22\sss.py"))
# print(os.path.basename(r"F:\py3_study\learnPython-master\Python基础代码\day22\sss.py"))

a="F:\py3_study\learnPython-master" #拼接的时候尽量不用+
b="Python基础代码\day22\sss.py"

print(os.path.join(a,b))  #路径拼接

print(os.path.getatime(os.path.join(a,b)))
print(os.path.getctime(os.path.join(a,b)))

# os.system() #以后不用 subprocess替代



