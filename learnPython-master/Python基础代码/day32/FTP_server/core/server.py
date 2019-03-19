# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/3/19 15:48
import socketserver
class SeverHandler(socketserver.BaseRequestHandler):
   def handle(self):
       print("ok")
