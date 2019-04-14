# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/3/19 15:04
# import socket
#
# sk=socket.socket
#
# sk.connect(("127.0.0.1",8080))
#
import optparse
import socket
import configparser #基于字典操作的模块 出现了accounts.cfg
import json

class ClientHandler():

    def __init__(self):
        self.op=optparse.OptionParser()
        self.op.add_option("-s","--server",dest="server")
        self.op.add_option("-P","--port",dest="port")
        self.op.add_option("-u","--username",dest="username")
        self.op.add_option("-p","--passowrd",dest="password")


        self.option,self.args=self.op.parse_args()

        self.verity_args(self.options,self.args)
        self.make_connection()

    def verify_args(self,options,args):
        server=options.server
        port=options.port
        # username=options.username
        # password=options.password

        if int(port)>0 and int(port)<65535:
            return True
        else:
            exit("the port is in 0-65535")


    def make_connection(self):
        self.sock=socket.socket()
        self.sock.connect((self.options.serve,int(self.options.port)))

    def interactive(self):
        self.authenticate()


    def authenticate(self):
        if self.options.username is None or self.options.password is None:
            username=intput("username:")
            password=input("password")
            return get_auth_result(username,password)
        return self.get_auth_result(self.options.username,self.options.password)

    def response(self):
        data = self.sock.recv(1024).decode("utf8")
        data = json.loads(data)
        return data


    def get_auth_result(self,user,pwd):

        data={
            "action":"auth",
            "username":user,
            "password":pwd



        }
        self.sock.send(json.dumps(data)).encode("utf8")
        response=self.response()
        print(response)








ch=ClientHandler()

ch.interactive()








