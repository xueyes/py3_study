# -*- coding=utf8 -*-
__author__ = 'admin'
#@Time :2019/1/10 15:11


import os


def file_handler(backend_data,res=None,type='fetch'): #程序的解耦
    if type == 'fetch':
    with open('haproxy.conf','r') as read_f:
        tag = False
        ret=[]
        for read_line in read_f:
            if read_line.strip() == backend_data:   #strip 默认去掉回车
                 tag=True #tag的方式去处理,标识一种状态
                 continue
            if tag and read_line.startswith('backend'):
                # tag=False
                break

            # if not tag:
            #     pass
            #
            if tag:
                print('\033[1;45m%s\033[0m' %read_line,end='')
                ret.append(read_line)
    return ret

    elif type == 'change':

        with open('haproxy.conf','r') as read_f,\
                open('haproxy.conf_new','w') as write_f:
                tag=False
                has_write=False
            for read_line in read_f:
                if read_line.strip() == backend_data:
                tag=True
                continue

                if tag and read_line.startswith('backend'):
                    tag=False


                if not tag:
                    write_f.write(read_line)
                else:
                    if not  has_write:
                    for record in res:
                        write_f.write(record)
                        has_write=True  #状态的变化控制流程


        os.rename('haproxy.conf', 'haproxy.conf.bak')
        os.rename('haproxy.conf_new', 'haproxy.conf')
        os.remove('haproxy.conf_bak')


def  fetch(data):
    # print('\033[1;43m这是查询功能\033[0m')
    # print('\033[1;43m用户数据是\033[0m',data)


    backend_data='backend %s'%data
    return file_handler(backend_data)



def add():
    pass



def change():
    print('这是修改功能')
    backend=data[0]['backend'] #文件当中的一条记录
    backend_data='backend %s' %backend  #backend www.oldboy.org
    old_server_record='%sserver %s %s weight %s maxconn %s\n' %(''*8,data[0]['record']['server'],
                                                              data[0]['record']['server'],
                                                              data[0]['record']['weight'],
                                                              data[0]['record']['maxconn'])



    new_server_record='%sserver %s %s weight %s maxconn %s\n' %(''*8,data[1]['record']['server'],
                                                              data[1]['record']['server'],
                                                              data[1]['record']['weight'],
                                                              data[1]['record']['maxconn'])
    print('用户想要修改的记录是%s'%old_server_record)
    res=fetch(backend) #fetch('www.oldboy1.org')
    print('来自change函数--》',res)
    if not res or  old_server_record not in res:
        return '你要修改的记录不存在'
    # if old_server_record not in res:
    else:
        index=res.index(old_server_record)
        res[index]=new_server_record            #新的值

    res.insert(0,'%s\n' %backend_data)
    file_handler(backend_data,res=res,type='change')


def delete():
    pass



if __name__ == '__main__':  #规范,python文件当中,应当只写功能,能够执行的代码只能在这个下面调用,以防止别人也用
    print('test')
    msg='''
    1:查询
    2：添加
    3：修改
    4：删除
    5：退出
    '''
    msg_dic={
        '1':fetch,
        '2':add,
        '3':change,
        '4':delete,
    }

    while True:
        print(msg)
        choice=input('请输入你的选项:').strip()
        if not choice:continue
        if choice=='5':break

        data=input('请输入你的数据:').strip()


        res=msg_dic[choice](data)
        print(res)


# print(__name__)

#函数、文件处理、tag、程序的解耦

