# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/9 17:57

# 京东后端就是一个个的功能
# 都装上一个验证功能
user_dic={'username':None,'login':False}


def auth_func(func):
    def wrapper(*args,**kwargs):
        if user_dic['username'] and user_dic['login']:
            res = func(*args, **kwargs)
            return res
        username=input('用户名:').strip()
        passwd=input('密码').strip()
        if username == 'sb' and passwd == '123':
            user_dic['username']=username
            user_dic['login']=True

            res=func(*args,**kwargs)
            return res
        else:
            print('用户名或者密码错误')
        return wrapper


@auth_func
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

