# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/9 15:37

#
# def  bar():
#     print('from bar')
#
# def foo():
#     print('from foo')
#
#     def test()
#         pass
# bar()


def father(name):
    #print("from father %s" %name)
    def son():
        print('from the son')
        #name='linhaifeng_1'
    son()
        print('我的爸爸是%s'%name)
    #print(locals()) #打印当前层的局部变量
        def grandson():
            name='就是我自己'
            print('我的爷爷是%s                                                                   ' %name)
        grandson()

father('linhaifeng')

