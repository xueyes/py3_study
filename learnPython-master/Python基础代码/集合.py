# -*- coding=utf8 -*-
__author__ = 'admin'

[1,'www',1,1]

#集合是将不同的元素组成在一起


#集合的创建

# a = [1,2,3,4]
#
# b=list([4,5,6])
# b1=tuple([7,8,9])
#
# print(a)
#
# print(b)
#
# print(b1)

s = set('alex li')
s1 = {'alvin','ee','alvin'}
s2=set(s1)
print(s2,type(s2))


s = list(s2)
print(s,type(s))

#可hash key(键) 不可变类型 字典和列表不可以

li = [2,3,'alex']

s = set(li) #整体是不可哈希的
print(s)

#set是无序的  for循环 diandaiqi

#可变集合,非可变集合

#d ={s:'123'} #TypeError: unhashable type: 'set'

print(2 in s)

print(4 in s )

for i in s:
    print(i)

# s.add('u')
# print(s)

# s.add('uu') #添加一个元素
# print(s)

# s.update('ooo') #更新并且保留原来的,ops相当于序列被添加
# print(s)
# s.update([12,'alex']) #更新并且保留原来的,ops相当于序列被添加  set不重复需要有迭代功能
#
# print(s)

# s.remove(2)
# print(s)

# s.pop() #随机删除除
# print(s)

# s.clear()
# print()


print(set('alex')==set('alexexex'))

print(set('alex')<set('alexwwww'))

print(set('alex') or set('alexwwww'))

print(set('alex') and set('alexwwww'))

print(set('alextq') or set('alexwwww'))

#










