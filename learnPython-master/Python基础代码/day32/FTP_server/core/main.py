# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/3/19 15:05
import optparse #解析命令行
import socketserver


from conf import settings
from core import server


class ArgvHandler():

    def __init__(self):
        self.op=optparse.OptionParser()

        #
        # self.op.add_option("-s","--server",dest="server")
        # self.op.add_option("-P","--port",dest="port")
        #
        #
        #
        options,args=self.op.parse_args()
        # print(type(options))
        # print(options.server)
        # print(options.port)
        # print(args)

        self.verify_args(options,args)
    def verify_args(self,options,args):

        cmd=args[0]

        # if cmd=="start"
        #     pass
        #
        # elif cmd==  low逼  而是用反射 #https://www.cnblogs.com/yyyg/p/5554111.html
        if hasattr(self,cmd):
            func=getattr(self,cmd)  #学会了反射就不要用if else 和字典
            func()

    def start(self):
        print("the server is working.....")
        s = socketserver.ThreadingTCPServer((settings.IP,settings.PORT), server.ServerHandler)
        s.serve_forever()



    def help(self):
        pass
















