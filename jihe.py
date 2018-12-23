#coding:utf8
#http://www.cnblogs.com/linhaifeng/articles/7133357.html
# 有如下两个集合，pythons是报名python课程的学员名字集合，linuxs是报名linux课程的学员名字集合


# pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
# linuxs={'wupeiqi','oldboy','gangdan'}
# 求出即报名python又报名linux课程的学员名字集合
# print(pythons & linuxs)
# 求出所有报名的学生名字集合
# print(pythons | linuxs)
# 求出只报名python课程的学员名字
# print(pythons - linuxs)
# 求出没有同时这两门课程的学员名字集合
# print(pythons ^ linuxs)



#去重,无需保持原来的顺序
# l=['a','b',1,'a','a']
# print(set(l))

#去重,并保持原来的顺序
#方法一:不用集合
# l=[1,'a','b',1,'a']
#
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)

#方法二:借助集合
# l1=[]
# s=set()
# for i in l:
#     if i not in s:
#         s.add(i)
#         l1.append(i)
#
# print(l1)


#同上方法二,去除文件中重复的行
# import os
# with open('db.txt','r') as read_f,\
#         open('.db.txt.swap','w') as write_f:
#     s=set()
#     for line in read_f:
#         if line not in s:
#             s.add(line)
#             write_f.write(line)
# os.remove('db.txt')
# os.rename('.db.txt.swap','db.txt')

#列表中元素为可变类型时,去重,并且保持原来顺序
l=[
    {'name':'egon','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'egon','age':20,'sex':'female'},
    {'name':'egon','age':18,'sex':'male'},
    {'name':'egon','age':18,'sex':'male'},
]
# print(set(l)) #报错:unhashable type: 'dict'


# s=set()
# print s
# l1=[]
# for item in l:
#     val=(item['name'],item['age'],item['sex'])
#     if val not in s:
#         s.add(val)
#         l1.append(item)
#
# print(l1)

# 定义函数,既可以针对可以hash类型又可以针对不可hash类型
def func(items,key=None):
    s=set()
    for item in items:
        val=item if key is None else key(item)
        if val not in s:
            s.add(val)
            yield item

print(list(func(l,key=lambda dic:(dic['name'],dic['age'],dic['sex']))))