#coding=utf8
_author_ = 'hashlinux'

# with open('a.txt') as f:
        #'代码块'

# with obj('a.txt') as f:
#1.with obj ----> 触发obj.__enter__(),拿到返回值

#2。as f ----->f=返回值

#3.with obj af f =====> 发= ojbj.enter__()

#4.执行代码块

#http://note.youdao.com/noteshare?id=f7e96bbc52ce1f15cfb6a7daee3d891a

# 上下文管理协议 with语句  open里面做手脚

class Open:
    def __init__(self,name):
        self.name=name


    def __enter__(self):
        print('执行enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('执行exit')
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True  #会吃掉异常


with Open('a.txt') as f:

    print(f)
    print(asdffggggggsss)  #触发exit
    print(f.name)

    print('-----------')
    print('-----------')
    print('-----------')
    print('-----------')
    print('-----------')
    print('000000000000')



