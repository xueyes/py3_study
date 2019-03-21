# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/3/19 15:48
import socketserver
import json
class SeverHandler(socketserver.BaseRequestHandler):
   def handle(self):

       while 1:
           #conn=self.requst
           data=self.request.recv(1024).strip()
           # data.decode("utf8")
           data=json.loads(data.decode("utf8"))

           """
           {"action":"auth",
           "username":"yuan"
           "pwd":123
           }
           """
           if data.get("action"):

               if hasattr(self,data.get("actions")):
                   func=getattr(self,data.get("action"))
                   func(**data)
               else:
                   print("invaid cmd")

           else:
                print("invaid cmd")

    def auth(self,**data):
        print("data",data)

    def put(self,**data):
















