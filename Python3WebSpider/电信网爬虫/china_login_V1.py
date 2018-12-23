import requests
from Cryptodome.Cipher import AES
import os
import execjs
import math
import boto3
from bs4 import BeautifulSoup
from urllib.parse import  urlencode
import random
from fake_useragent import UserAgent
from http.cookiejar import CookieJar
import re
import json
import time


class Login(object):
    def __init__(self):
        self.UserAgent = UserAgent().random
        print(self.UserAgent)
        #构建headers
        self.headers = {
            'Referer': 'http://login.189.cn/web/login',
            'User-Agent': self.UserAgent,
            'Host': 'login.189.cn'
        }
        #登录url
        self.login_url = "http://login.189.cn/web/login"
        #已经登录的url
        # self.logined_url = "http://www.189.cn/gz/"
        self.session = requests.Session()
        self.client = boto3.client('rekognition', region_name="us-east-2",
                              aws_access_key_id="AKIAJOE4GFCNJ6MOZODA",
                              aws_secret_access_key="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")
        self.proxies = self.get_proxies()

    # def get_session(self):
    #     session = requests.session()
    #     # session.headers = headers
    #     # session.cookies = MozillaCookieJar()
    #     return session
    def get_proxies(self):
        str_ip = """ 45.57.186.217:3128
                    192.227.149.37:3128
                    196.19.63.92:3128
                    179.43.138.98:3128
                    45.57.186.161:3128
                    196.17.143.233:3128
                    45.57.186.179:3128
                    192.126.129.224:3128
                    196.16.208.83:3128
                    192.126.129.181:3128
                    192.227.149.166:3128
                    196.17.143.220:3128
                    179.43.138.195:3128
                    179.43.138.155:3128
                    196.19.70.182:3128
                    196.19.63.253:3128
                    192.227.149.179:3128
                    196.19.70.20:3128
                    196.17.128.178:3128
                    192.126.199.41:3128
                    196.17.131.113:3128
                    192.126.199.24:3128
                    45.33.156.236:3128
                    216.158.208.87:3128
                    196.16.38.81:3128
                    192.126.249.159:3128
                    196.16.36.163:3128
                    45.33.156.43:3128
                    196.17.128.171:3128
                    192.126.249.118:3128
                    196.16.36.208:3128
                    196.16.38.60:3128
                    216.158.208.217:3128
                    196.17.131.136:3128
                    196.16.36.102:3128
                    196.17.131.74:3128
                    196.17.128.157:3128
                    192.126.199.110:3128
                    196.16.36.48:3128
                    216.158.208.78:3128
                    196.16.38.193:3128
                    196.17.128.91:3128
                    196.17.131.199:3128
                    192.126.249.33:3128
                    216.158.208.82:3128
                    192.126.199.118:3128
                    192.126.249.206:3128
                    45.33.156.116:3128
                    192.126.199.130:3128
                    192.126.199.62:3128
                    192.126.249.13:3128
                    196.17.131.150:3128
                    45.33.156.103:3128
                    196.17.128.124:3128
                    45.33.156.176:3128
                    216.158.208.246:3128
                    216.158.208.128:3128
                    196.16.38.108:3128
                    192.126.199.251:3128
                    45.33.156.242:3128
                    192.126.249.69:3128      
        
        """
        list_ip = str_ip.replace("\n", ",").split(",")
        # print(list_ip)
        ip = str(random.choice(list_ip)).strip()
        # print(ip)
        proxies = {
            'http': 'http://%s' % ip,
            'https': 'https://%s' % ip
        }
        return proxies

    #使用node引擎执行加密的密码
    def decode_password(self,password):
        #本地安装的node  path 的路径
        os.environ["NODE_PATH"] = 'E:/python3.6.1/Tools/node_v7.6.0/node_modules/'
        #查看是否配置是Node.js (V8)，确保配置没有问题
        print(execjs.get().name)

        parser = execjs.compile("""
            var CryptoJS = require("crypto-js");

            function encryption(password) {
            console.log('aesEncrypt text: ' + password)
            var t = CryptoJS.MD5("login.189.cn"),
        	    i = CryptoJS.enc.Utf8.parse(t),
                r = CryptoJS.enc.Utf8.parse("1234567812345678"),
        		u = CryptoJS.AES.encrypt(password, i, {iv: r});
            return u + ""
        }
        """)
        objpassword = parser.call("encryption", password)
        return objpassword

    #获取验证码
    def get_captcha(self):
        image_link = "http://login.189.cn/web/captcha?undefined&source=login&width=100&height=37&"
        response = self.session.get(url=image_link, headers =self.headers)
        with open("./code.png","wb") as fn:
            fn.write(response.content)
        captcha = input("请输入验证码：")
        return  captcha

    """
    电信网返回成功登录的URL不一样，应该是设置了，所以暂时不做任何处理，返回什么是什么
    """
    def login(self, usename, password):

        login_headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://login.189.cn/web/login',
            'User-Agent': self.UserAgent,
            'Host': 'login.189.cn',
            'Origin': 'http://login.189.cn',
            'Cache-Control':'max-age=0',
            'Content-Length':'125',
            'Upgrade-Insecure-Requests':'1',
            # 'Cookie':'code_v=20170913; svid=9A23FFBDE1BBB9D8; s_fid=4AA7EBAE5B7E02EB-3C572ECFDE1A0C1B; lvid=bf7c606df147cb3d9e6e237d9e1815e4; nvid=1; trkId=41B8FA5D-242D-407D-8C0B-A20E3F89203D; pgv_pvid=3232119000; dqmhIpCityInfos=%E8%B4%B5%E5%B7%9E%E7%9C%81%E8%B4%B5%E9%98%B3%E5%B8%82+%E7%94%B5%E4%BF%A1; ECS_ReqInfo_get_yw=U2FsdGVkX19tUGIpFMln6a9qFYSFVqYt4QRe2S%2FV7tU%3D; NTKF_T2D_CLIENTID=guest0A96EDF1-0AA5-25EB-6C0E-7C9A91912CE6; ECS_ReqInfo_get=U2FsdGVkX1%2FmQfppeGkLHYUPXJ2XJcDNn5XMB29N0Sg%3D; s_cc=true; __qc_wId=962; EcsCaptchaKey=mRH2wEXZIyrNtyLu9%2FT2U%2FrldjbIXcyE%2F6u%2F58RVb6SP5OQrMMynJw%3D%3D; SHOPID_COOKIEID=10011; cityCode=js_nj; nTalk_CACHE_DATA={uid:kf_9643_ISME9754_guest0A96EDF1-0AA5-25,tid:1544511824327122}; _jzqa=1.1520266124683238400.1544405723.1544413832.1544511825.4; _jzqc=1; _jzqx=1.1544405723.1544511825.1.jzqsr=js%2E189%2Ecn|jzqct=/index%2Ejsp.-; _jzqckmp=1; _jzqb=1.1.10.1544511825.1; oldtime=17877; trkHmPageName=%2Fgz%2F; aactgsh111220=17385314488; userId=201%7C20170100000075540603; .ybtj.189.cn=FE8E191EFDC6D1545DB2C3D5B7EC98DC; trkHmCoords=0; trkHmCity=0; trkHmLinks=0; isLogin=non-logined; s_sq=%5B%5BB%5D%5D; loginStatus=non-logined; EcsToLoginPara=zBPyOxHfMwekoO0uXkKvuYa0LkztAQUHUJWySfbGejrRbvwHNni8ykV06E3z37guaQUBgIws5azzfVbc3wrOIjzPXSY2XOVg9yX4M3RtdgMnEKrCBz3GOlfwqPECYc8nEP9je35oVUE%3D; ECS_ReqInfo_login1=U2FsdGVkX1%2BJE9m%2F2N1IjEPkliOKCTdDEqpBUVV%2Fe5cquoMkxac4KCvYaMBEP6DyofVT9mc%2B3Uamjf1ZPC%2F81tDVjFuenT0bG8nZrbsNCFU%3D; trkHmClickCoords=739%2C449%2C682'

        }

        #待完成ProvinceID 的值
        post_data = {
            'Account': usename,
            'UType': '201',
            'ProvinceID':'24',
            'AreaCode':'',
            'CityNo':'',
            'RandomFlag': '0',
            'Password': self.decode_password(password),
            'Captcha': self.get_captcha(),
        }

        #登入的post请求
        # response = self.session.post(self.login_url, data=post_data, headers=login_headers, proxies= self.proxies)
        response = self.session.post(self.login_url, data=post_data, headers=login_headers)

        #返回登录的url
        logined_url = response.url

        #CookieJar可以帮我们自动处理Cookie
        # self.session.cookies=CookieJar()

        return logined_url
    """
用户姓名            
证件号               
手机号                              
开卡日期
联系地址
其它联系人姓名
其它联系电话
    """
    def get_Personal_BasicInfo(self,cook):
        headers = {
            'User-Agent': self.UserAgent,
            'Cookie':cook
        }

        url = "http://www.189.cn/dqmh/userCenter/userInfo.do?method=editUserInfo"

        response = self.session.get(url = url,headers=headers)
        html = response.text
        # print(html)
        soup = BeautifulSoup(html, "lxml")
        personalInfo = {}
        dict = {}
        dict["realName"] = soup.select('#realnameTd input')[0].attrs['value']
        dict["certificateNumber"] = soup.select('#cardnumTd input')[0].attrs['value']
        dict["otherphoneNumber"] = soup.select('#phoneNumberTd input')[0].attrs['value']
        dict["userphoneNumber"] = soup.select('#personalInfo td span')[0].get_text().strip()
        print(dict)
        address_end = soup.select('#addressTd  textarea')[0].get_text().strip()
        print(address_end)
        try:
            # 地址单独处理
            try:

                #获取地址信息
                list_addr = soup.select('form td script')[1].get_text().strip()
                list_addr = list_addr.split(";")

                #获取def_province_code 省份代码，使用正则表达式匹配
                str_province_code = str(list_addr[0])
                def_province_code = re.findall(r'def_province_code = "(.*?)"', str_province_code)[0]
                print(def_province_code)

                # dict_def_province_code ={
                #     '002024':'安徽',
                #     '002001':'北京',
                #     '002040':'重庆',
                #     '002025':'福建',
                #     '002052':'甘肃',
                #     '002034':'广东',
                #     '002035':'广西',
                #     '002042':'贵州',
                #     '002036':'海南',
                #     '002003':'河北',
                #     '002031':'河南',
                #     '002013':'黑龙江',
                #     '002032':'湖北',
                #     '002033':'湖南',
                #     '002012':'吉林',
                #     '002022':'江苏',
                #     '002026':'江西',
                #     '002011':'辽宁',
                #     '002005':'内蒙古',
                #     '002054':'宁夏',
                #     '002053':'青海',
                #     '002027':'山东',
                #     '002004':'山西',
                #     '002051':'陕西',
                #     '002021':'上海',
                #     '002041':'四川',
                #     '002002':'天津',
                #     '002044':'西藏',
                #     '002055':'新疆',
                #     '002043':'云南',
                #     '002023':'浙江'
                # }
                #省份添加到地址列表中
                # addr.append(dict_def_province_code[def_province_code])

                #获取def_city_code
                # def_city_code 城市代码，使用正则表达式匹配
                str_city_code = str(list_addr[1]).strip()
                def_city_code = re.findall(r'def_city_code = "(.+?)"', str_city_code)[0]
                print(def_city_code)

                #获取def_country_code 区域代码，使用正则表达式匹配
                str_country_code = str(list_addr[2]).strip()
                def_country_code = re.findall(r'def_country_code = "(.*?)"', str_country_code)[0]
                print(def_country_code)

                #共同的url
                code_baseurl = 'http://www.189.cn/dqmh/integrated/orderInfo.do?'

                # 获取省份json 数据
                querytime = str(time.time()).replace('.', '')[:13]
                params_province = {
                    'method': 'getAreaInfo',
                    'area': 'province',
                    'timeflg': querytime
                }

                province_url = code_baseurl + urlencode(params_province)
                print(province_url)
                province_res = self.session.get(url = province_url,headers=headers)
                province_jsondata = province_res.text
                province_jsondata = json.loads(province_jsondata)
                province_list = province_jsondata["dataObject"]
                province_dict = {}
                for province_code in province_list:
                    province_dict[province_code['freight_area_code']] = province_code['freight_area_name']
                print(province_dict)

                dict_province = {}

                # 获取城市json 数据
                params_city = {
                    'method': 'getAreaInfo',
                    'area': 'city',
                    'timeflg': querytime,
                    'province':def_province_code

                }

                city_url = code_baseurl + urlencode(params_city)
                print(city_url)
                city_res = self.session.get(url = city_url,headers=headers)
                city_jsondata = city_res.text
                city_jsondata = json.loads(city_jsondata)
                city_list = city_jsondata["dataObject"]
                print()
                city_dict = {}
                for city_code in city_list:
                    city_dict[city_code['freight_area_code']] = city_code['freight_area_name']
                print(city_dict)

                # 获取区域json 数据
                params_county = {
                    'method': 'getAreaInfo',
                    'area': 'county',
                    'timeflg': querytime,
                    'city':def_city_code,
                    'province': def_province_code

                }

                county_url = code_baseurl + urlencode(params_county)
                print(county_url)
                county_res = self.session.get(url = county_url,headers=headers)
                county_jsondata = county_res.text
                county_jsondata = json.loads(county_jsondata)
                print()
                county_list = county_jsondata["dataObject"]
                county_dict = {}
                for county_code in county_list:
                    county_dict[county_code['freight_area_code']] = county_code['freight_area_name']
                print(county_dict)


                dict["address"] = province_dict[def_province_code] + city_dict[def_city_code] + county_dict[def_country_code] + address_end
                print(dict)

            except:
                dict["address"] = None
        except:
            pass

    #    cook = 'svid=9A23FFBDE1BBB9D8; s_fid=4AA7EBAE5B7E02EB-3C572ECFDE1A0C1B; lvid=bf7c606df147cb3d9e6e237d9e1815e4; nvid=1; trkId=41B8FA5D-242D-407D-8C0B-A20E3F89203D; dqmhIpCityInfos=%E8%B4%B5%E5%B7%9E%E7%9C%81%E8%B4%B5%E9%98%B3%E5%B8%82+%E7%94%B5%E4%BF%A1; NTKF_T2D_CLIENTID=guest0A96EDF1-0AA5-25EB-6C0E-7C9A91912CE6; _jzqa=1.1520266124683238400.1544405723.1544413832.1544511825.4; _jzqx=1.1544405723.1544511825.1.jzqsr=js%2E189%2Ecn|jzqct=/index%2Ejsp.-; oldtime=17877; SHOPID_COOKIEID=10024; cityCode=gz; userId=201%7C20170100000075540603; .ybtj.189.cn=FE8E191EFDC6D1545DB2C3D5B7EC98DC; aactgsh111220=17385314488; s_cc=true; PHPSESSID=o6qpa27tj8kga8lpl69k6umg09; trkHmCoords=0; trkHmCity=0; trkHmLinks=0; trkHmCitycode=0; trkHmPageName=0; isLogin=logined; loginStatus=logined; trkHmClickCoords=0; s_sq=%5B%5BB%5D%5D'
    #    cook = 'svid=9A23FFBDE1BBB9D8; s_fid=4AA7EBAE5B7E02EB-3C572ECFDE1A0C1B; lvid=bf7c606df147cb3d9e6e237d9e1815e4; nvid=1; trkId=41B8FA5D-242D-407D-8C0B-A20E3F89203D; dqmhIpCityInfos=%E8%B4%B5%E5%B7%9E%E7%9C%81%E8%B4%B5%E9%98%B3%E5%B8%82+%E7%94%B5%E4%BF%A1; NTKF_T2D_CLIENTID=guest0A96EDF1-0AA5-25EB-6C0E-7C9A91912CE6; _jzqa=1.1520266124683238400.1544405723.1544413832.1544511825.4; _jzqx=1.1544405723.1544511825.1.jzqsr=js%2E189%2Ecn|jzqct=/index%2Ejsp.-; oldtime=17877; SHOPID_COOKIEID=10024; cityCode=gz; s_cc=true; PHPSESSID=o6qpa27tj8kga8lpl69k6umg09; trkHmCoords=0; trkHmCity=0; trkHmLinks=0; trkHmCitycode=0; trkHmPageName=0; aactgsh111220=17785395847; userId=201%7C20170100000028281982; .ybtj.189.cn=2DE0B2A31693DB526FD113A7844367F8; isLogin=logined; loginStatus=logined; trkHmClickCoords=0; s_sq=%5B%5BB%5D%5D'

    #用户最近3个月的通话详单
    def get_CalldetailsInfo(self,cook):
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Host':'service.gz.189.cn',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent': self.UserAgent,
            'Cookie': cook,
            'Referer':'http://service.gz.189.cn/web/query.php?action=call',
            'X-Requested-With':'XMLHttpRequest'
        }

        url = "http://service.gz.189.cn/web/query.php?action=call"
        response = self.session.get(url=url,headers=headers)
        html = response.text

        soup = BeautifulSoup(html, "lxml")
        QueryMonthlyInfo = soup.select('#QueryMonthly label')
        # print(QueryMonthlyInfo)
        #获取前3个月
        month1 = QueryMonthlyInfo[0].get_text().strip()
        month2 = QueryMonthlyInfo[1].get_text().strip()
        month3 = QueryMonthlyInfo[2].get_text().strip()
        # print(month1)
        # print(month2)
        # print(month3)

        #最近3个月的入list列表
        QueryMonthly = []
        QueryMonthly.append(month1)
        QueryMonthly.append(month2)
        QueryMonthly.append(month3)

        #用于保存最近3个月的通话详单
        CalldetailsInfodict = {}

        for querymonthly in QueryMonthly:
            print(querymonthly)

            #添加一个时间戳
            querytime = str(time.time()).replace('.', '')[:13]
            # 构造查询的url
            params = {
                'action':'getAllCall',
                'QueryMonthly':querymonthly,
                'QueryType':'1',
                'checkcode':'undefined',
                '_':querytime
            }
            basic_url = 'http://service.gz.189.cn/web/query.php?'
            query_url = basic_url + urlencode(params)
            print(query_url)

            query_res = self.session.get(url=query_url,headers=headers)
            resultsCalldetailsInfo = query_res.text
            #resultsCalldetailsInfo["CALLING_TYPE_NAME"] = resultsCalldetailsInfo["CALLING_TYPE_NAME"].encode().decode('utf-8')
            print(resultsCalldetailsInfo)
            CalldetailsInfodict[querymonthly + '-' + 'CalldetailsInfo'] = resultsCalldetailsInfo

        return CalldetailsInfodict


    #查询用户余额
    def get_balance(self):
        cook = 'svid=9A23FFBDE1BBB9D8; s_fid=4AA7EBAE5B7E02EB-3C572ECFDE1A0C1B; lvid=bf7c606df147cb3d9e6e237d9e1815e4; nvid=1; trkId=41B8FA5D-242D-407D-8C0B-A20E3F89203D; dqmhIpCityInfos=%E8%B4%B5%E5%B7%9E%E7%9C%81%E8%B4%B5%E9%98%B3%E5%B8%82+%E7%94%B5%E4%BF%A1; NTKF_T2D_CLIENTID=guest0A96EDF1-0AA5-25EB-6C0E-7C9A91912CE6; s_cc=true; PHPSESSID=its84sm8856eh7g1etf15lla2h; nTalk_CACHE_DATA={uid:kf_9643_ISME9754_guest0A96EDF1-0AA5-25,tid:1544511824327122}; _jzqa=1.1520266124683238400.1544405723.1544413832.1544511825.4; _jzqc=1; _jzqx=1.1544405723.1544511825.1.jzqsr=js%2E189%2Ecn|jzqct=/index%2Ejsp.-; _jzqckmp=1; oldtime=17877; userId=201%7C20170100000075540603; .ybtj.189.cn=FE8E191EFDC6D1545DB2C3D5B7EC98DC; SHOPID_COOKIEID=10024; cityCode=gz; trkintaid=gz-sy-hxfw-04-; trkHmCitycode=0; trkHmCoords=0; trkHmCity=0; trkHmLinks=0; trkHmPageName=0; loginStatus=logined; trkHmClickCoords=0; s_sq=%5B%5BB%5D%5D'
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Host':'service.gz.189.cn',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent': self.UserAgent,
            'Cookie': cook
        }

        # 用户选择的话费套餐金额  baseLink待优化
        baseLink = 'http://service.gz.189.cn/web2.0/query2.php?action=mybill'
        response_balance = self.session.get(url=baseLink, headers=headers)
        html_balance = response_balance.text
        soup_balance = BeautifulSoup(html_balance, "lxml")
        balance = soup_balance.select('td.time  span')[1].get_text().strip()
        print(balance)
        return balance


    #查询用户最近6个月的账单记录
    def get_BillingrecordsInfo(self):
        cook = 'svid=9A23FFBDE1BBB9D8; s_fid=4AA7EBAE5B7E02EB-3C572ECFDE1A0C1B; lvid=bf7c606df147cb3d9e6e237d9e1815e4; nvid=1; trkId=41B8FA5D-242D-407D-8C0B-A20E3F89203D; dqmhIpCityInfos=%E8%B4%B5%E5%B7%9E%E7%9C%81%E8%B4%B5%E9%98%B3%E5%B8%82+%E7%94%B5%E4%BF%A1; NTKF_T2D_CLIENTID=guest0A96EDF1-0AA5-25EB-6C0E-7C9A91912CE6; s_cc=true; PHPSESSID=its84sm8856eh7g1etf15lla2h; nTalk_CACHE_DATA={uid:kf_9643_ISME9754_guest0A96EDF1-0AA5-25,tid:1544511824327122}; _jzqa=1.1520266124683238400.1544405723.1544413832.1544511825.4; _jzqc=1; _jzqx=1.1544405723.1544511825.1.jzqsr=js%2E189%2Ecn|jzqct=/index%2Ejsp.-; oldtime=17877; SHOPID_COOKIEID=10024; cityCode=gz; trkHmCitycode=0; aactgsh111220=17385314488; userId=201%7C20170100000075540603; .ybtj.189.cn=FE8E191EFDC6D1545DB2C3D5B7EC98DC; trkintaid=1; trkHmCoords=0; trkHmCity=0; trkHmLinks=0; trkHmPageName=0; isLogin=logined; loginStatus=logined; trkHmClickCoords=0; s_sq=%5B%5BB%5D%5D'
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Host':'service.gz.189.cn',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent': self.UserAgent,
            'Cookie': cook
        }


        #用户的账单记录
        paycheckLink = 'http://service.gz.189.cn/web2.0/query2.php?action=check'
        response_paycheck = self.session.get(url=paycheckLink, headers=headers)
        html_paycheck = response_paycheck.text
        soup_paycheck = BeautifulSoup(html_paycheck, "lxml")

        #获取最近6个月的月份
        month = soup_paycheck.select('ul#selmon li')   #获取最近6个月的集合
        #获取最近的月份
        month1 = month[0].get_text().strip()
        month2 = month[1].get_text().strip()
        month3 = month[2].get_text().strip()
        month4 = month[3].get_text().strip()
        month5 = month[4].get_text().strip()
        month6 = month[5].get_text().strip()
        print(month)
        headerspost = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection':'keep-alive',
            'Content-Length':'12',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'service.gz.189.cn',
            'Origin':'http://service.gz.189.cn',
            'Referer':'http://service.gz.189.cn/web2.0/query2.php?action=check',
            'User-Agent': self.UserAgent,
            'Cookie': cook,
            'X-Requested-With':'XMLHttpRequest'

        }

        month_list = []
        month_list.append(month1)
        month_list.append(month2)
        month_list.append(month3)
        month_list.append(month4)
        month_list.append(month5)
        month_list.append(month6)

        dict_BillingrecordsInfo = {}
        for monthpost in month_list:
            print(monthpost)
            post_data = {
                'month': monthpost
            }

            post_url = 'http://service.gz.189.cn/web2.0/query2.php?action=getcheck'
            BillingrecordsInfo = self.session.post(url=post_url, data=post_data, headers=headerspost)

            html = BillingrecordsInfo.text
            print(html)
            jsonhtml = json.loads(html)

            message = jsonhtml['message']
            print(message)

            # 判断查询是否成功
            if message =="\u67e5\u8be2\u6210\u529f":
                productInfohtml = jsonhtml['productInfo']
                soup_productInfo = BeautifulSoup(productInfohtml, "lxml")

                # 当月实际话费合计
                costotal = soup_productInfo.select('p')[0].get_text().strip()
                print(costotal)
                dict_BillingrecordsInfo[monthpost] = costotal
                print(dict_BillingrecordsInfo)
            else:

                dict_BillingrecordsInfo[monthpost] = "queryfails"

        print(dict_BillingrecordsInfo)
        return dict_BillingrecordsInfo


if __name__=="__main__":
    china_loin = Login()
    # logined_url= china_loin.login("17385314488","580748")
    # print(logined_url)
    cook = 'svid=9A23FFBDE1BBB9D8; s_fid=4AA7EBAE5B7E02EB-3C572ECFDE1A0C1B; lvid=bf7c606df147cb3d9e6e237d9e1815e4; nvid=1; trkId=41B8FA5D-242D-407D-8C0B-A20E3F89203D; dqmhIpCityInfos=%E8%B4%B5%E5%B7%9E%E7%9C%81%E8%B4%B5%E9%98%B3%E5%B8%82+%E7%94%B5%E4%BF%A1; NTKF_T2D_CLIENTID=guest0A96EDF1-0AA5-25EB-6C0E-7C9A91912CE6; _jzqa=1.1520266124683238400.1544405723.1544413832.1544511825.4; _jzqx=1.1544405723.1544511825.1.jzqsr=js%2E189%2Ecn|jzqct=/index%2Ejsp.-; oldtime=17877; SHOPID_COOKIEID=10024; cityCode=gz; s_cc=true; trkHmCoords=0; trkHmCity=0; trkHmLinks=0; trkHmCitycode=0; trkHmPageName=0; PHPSESSID=4vt6ohm4gj8id8arpccjat2jc7; aactgsh111220=17785395847; userId=201%7C20170100000028281982; isLogin=logined; .ybtj.189.cn=2DE0B2A31693DB526FD113A7844367F8; loginStatus=logined; trkHmClickCoords=0; s_sq=%5B%5BB%5D%5D'

     # html = china_loin.get_Personal_BasicInfo(cook)
    # print(res)
    # print(html)
    # print(urled)

    CalldetailsInfodict = china_loin.get_CalldetailsInfo(cook)
    print(CalldetailsInfodict)
    # print(str(CalldetailsInfodict).decode())
    # china_loin.get_BillingrecordsInfo()
    # china_loin.get_balance()

    # china_loin.get_CallInfo()
    # dict = china_loin.get_Personal_BasicInfo()
    # print(dict)
    # # password = china_loin.decode_password("580748")
    # captcha = china_loin.get_captcha()
    # print(captcha)
    # # print(password)




