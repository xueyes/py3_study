#created by hash
#coding:utf8
#strip
name='*bob**'
print(name.strip('*'))
print(name.lstrip('*'))
print(name.rstrip('*'))

#lower,upper
name='bob'
print(name.lower())
print(name.upper())

#startswith,endswith
name='hash_SB'
print(name.endswith('SB'))
print(name.startswith('hash'))

#format的三种玩法
res='{} {} {}'.format('bob',18,'male')
res='{1} {0} {1}'.format('bob',18,'male')
res='{name} {age} {sex}'.format(sex='male',name='bob',age=18)

#split
name='root:x:0:0::/root:/bin/bash'
print(name.split(':')) #默认分隔符为空格
name='C:/a/b/c/d.txt' #只想拿到顶级目录
print(name.split('/',1))

name='a|b|c'
print(name.rsplit('|',1)) #从右开始切分

#join
tag=' '
print(tag.join(['bob','say','hello','world'])) #可迭代对象必须都是字符串

#replace
name='hash say :i have one tesla,my name is hash'
print(name.replace('hash','SB',1))

#isdigit：可以判断bytes和unicode类型,是最常用的用于于判断字符是否为"数字"的方法
age=input('>>: ')
print(age.isdigit())

