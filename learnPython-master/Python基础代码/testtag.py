# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/10 15:35
tag=True
while tag:   #想从第三级退出到第一次 true=tag
    print('level ')
    choice=input("level1:").strip()
    if choice == 'quit':break
    if choice == 'quit_all': tag = False
    while tag:
        print('level2')
        choice = input("level2>>: ").strip()
        if choice == 'quit': break
        if choice == 'quit_all': tag = False
        while tag:
            print('level3')
            choice = input("level3>>: ").strip()
            if choice == 'quit': break
            if choice == 'quit_all': tag = False


if choice =='quit_all':tag=False
