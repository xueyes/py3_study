#coding=utf8
#简单购物车,要求如下：
#实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入　　

msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}


goods_1 = []

while True:
    for key,item in msg_dic.items():
        print('name:{name}, price:{price}'.format(price=item,name=key))
        choice=input('商品>>:').strip()
        if not choice or choice not in msg_dic:continue
        count=input('个数>>:').strip()
        if not count.isdight():continue
        goods_1.append((choice,msg_dic[choice],count))

        print(goods_1)