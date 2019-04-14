# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/2/28 17:22

import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('10.10.20.174',6666)) #用linux服务器测试

phone.send('hello'.encode('utf-8'))


data=phone.recv(1024)

print('手动服务端的发来的消息:',data)



