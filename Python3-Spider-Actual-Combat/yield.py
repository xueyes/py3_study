# -*- coding=utf8 -*-
__author__ = 'admin'

# def count(n):
#     while n > 0:
#         yield n
#         n -=1
def count(n):
    print("counting")
    while n > 0:
        yield n
        n = 1
