import urllib.request
import re

'''
匹配演员列表
'''
url = 'https://movie.douban.com/subject/26260853/celebrities'
r = urllib.request.urlopen(url)
#print(r)

html = r.read().decode('utf-8')
#
# print(html)
# <a href="https://movie.douban.com/celebrity/1041020/">范·迪塞尔</a>

result2 = re.findall(r'(?<=title=").\S+', html)
#print(result2)

result2.pop() #相当于把作品的名字去掉了


result3 = sorted(set(result2), key=result2.index)
print(result3)
