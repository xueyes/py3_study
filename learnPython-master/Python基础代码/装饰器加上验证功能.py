# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/9 17:57

# 京东后端就是一个个的功能
# 都装上一个验证功能

user_list=[
    {'name':'alex','passwd':'123'},
    {'name':'linhaifeng','passwd':'123'},
    {'name':'wupeiqi','passwd':'123'},
    {'name':'yuanhao','passwd':'123'},
]

current_dic={'username':None,'login':False}

de auth(auth_type='filedb'):
def auth_func(func):
    def wrapper(*args,**kwargs):
        print('认证类型是%s' %name)
        for user_dic in user_list:

            res = func(*args, **kwargs)
            return res
        username=input('用户名:').strip()
        passwd=input('密码').strip()
        if user_dic['username'] and user_dic['login']:
            current_dic['username']=username
            current_dic['login']=True

            res=func(*args,**kwargs)
            return res
        else:
            print('用户名或者密码错误')
    return wrapper


@auth(auth_type='filedb')
def index():
    print('欢迎来到京东')


@auth_func
def home(name):
    print('欢迎回家%s'%(name))


@auth_func
def shooping_car(name):
    print('%s的购物车里有【%s,%s,%s】'%(name,'奶茶','妹妹','娃娃'))


index()
home('产品经理')
shooping_car('产品经理')

#每一次一刷新都要输入用户密码，这不科学

