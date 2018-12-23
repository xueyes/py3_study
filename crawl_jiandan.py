#conding:utf8
#第三方库
#request,beautifulsoup4

import requests,urllib.request
from bs4 import BeautifulSoup

#伪装

url = 'http://jandan.net/ooxx/page-77'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
source_code = requests.get(url,headers = header) #get html
#print(source_code)

plain_text = source_code.text
# print(plain_text)

#比较经典的写法
Soup = BeautifulSoup(plain_text)
#print(Soup)

download_links = []
folder_path = 'F:\py3_study\spider'

for pic_tag in Soup.find_all('img'):
    #print(pic_tag)
    pic_link = pic_tag.get('src')
    print(pic_link)

    download_links.append(pic_link)

#print(download_links)

for item in download_links:
    print(item)
    urllib.request.urlretrieve(item,folder_path + item[-5:])
    print(done)

