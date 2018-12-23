#coding:utf8

#字典
#作用：存多个值,key-value存取，取值速度快

#定义：key必须是不可变类型，value可以是任意类型
#1 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中

#即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}

# a = {'k1':[],'k2':[]}
# c = [11,22,33,44,55,66,77,88,99]
#
# for i in c:
#     if i >66:
#         a['k1'].append(i)
#     else:
#         a['k2'].append(i)
#
# print(a)


#统计单词的个数
#结果如：{'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}
s='hello alex alex say hello sb sb'

#第一种
# l = s.split()
# dic={}
# for item in l:
#     if item in dic:
#         dic[item]+=1
#     else:
#         dic[item]=1
#         print(dic)




#第二种 个人比较理解
# dic={}
# words=s.split()
# print(words)
# for word in words:
#     dic[word]=s.count(word)
#     print(dic)


#第三种
#利用setdefault解决重复赋值
'''
setdefault的功能
1：key存在，则不赋值，key不存在则设置默认值
2：key存在，返回的是key对应的已有的值，key不存在，返回的则是要设置的默认值
d={}
print(d.setdefault('a',1)) #返回1

d={'a':2222}
print(d.setdefault('a',1)) #返回2222
'''

# dic={}
# words=s.split()
# for word in words:
#     dic.setdefault(word,s.count(word))
#     print(dic)

#第四种
#利用集合，去掉重复，减少循环次数
s='hello alex alex say hello sb sb'
dic={}
words=s.split()
words_set=set(words)
for word in words_set:
    dic[word]=s.count(word)
    print(dic)



