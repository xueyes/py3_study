#coding=utf8
_author_ = 'hashlinux'
#后面还需要学习前端， 数据交换 json其实是在js里面提取出来的概念

# dic='{"name":"alex"}'
# f=open("hello","w")
# f.write(dic)
#
# f_read=open("hello","r")
# data=f_read.read()
# print(type(data))
# data=eval(data)
# print(data["name"])
# import json
# dic={"name":"alex"} #所有的数据类型一定会被变成双引号 {"name": "alex"}

# data=json.dumps(dic)
# print(data)
# print(type(data))
# i=8   #-->"8"
# s='hello'  #--->"hello"
# l=[11,22]   #---->"[11,22]"
#
# # dic_str= json.dumps(dic)
# f=open("new_hello","w")
# f.write(dic_str)  #json.dump(dic,f) #文件处理的时候

# f_read=open("new_hello","r")
# # f_read.read()
# data=json.loads(f_read.read()) #data=json.load(f) 以后最大可能用loads,这仅用于文件操作
# print(data)
# print(type(data))

#注意
# import json
#
# with open("Json_test","r") as f:  #只要符合json字符串可以不用json.dump
#     data=f.read()
#     data=json.loads(data)
#     print(data["name"])

import pickle
dic = {'name':'alvin','age':23,'sex':'male'}
print(type(dic))

j= pickle.dumps(dic)
print(type(j))
#序列化 dumps

f = open('序列化对象_pickle','wb')
f.write(j)


#反序列化 load的是
f = open('反序列化_pickle','wb')  #pickle支持得多,但是一般用额是json




