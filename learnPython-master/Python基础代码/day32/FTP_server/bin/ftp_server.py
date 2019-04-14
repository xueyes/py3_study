# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/3/19 15:05

import os,sys

PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)


from  core import main


if __name__ == '__main__':

    main.ArgvHandler()





