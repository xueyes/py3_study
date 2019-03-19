# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/3/19 15:38
import socketserver

class Mysocket(socketserver.BaseRequestHandler):

    def handle(self):

        pass

s=socketserver.ThreadingTCPServer((),Mysocket)

s.serve_forever()

