# -*- coding=utf8 -*-
__author__ = 'admin'
import pyecharts

def demoa(data):
    es = pyecharts.EffectScatter("")
    flag = 0
    for title in data.items():
            if title[1] < 10: pass
            es.add(title[0],
                   [flag],
                   [title(1)],
                   symbol_size=10,
                   effect_scale=3.5,
                   symbol = "roundRect")
            flag += 1
    es.render()

def demob(data):
    es = pyecharts.Bar("")
    flag = 1
    for title in fata.items():
        if title[1] < 10: pass
        es.add(title[0],[flag],[title[1]])
        flag += 1
    es.render()


def democ(data):
    es = pyecharts.Pie("")
    sum = 0
    for i in data.values():
        sum += 1
    print(sum)
    flag = 1
    for title in data.items():
        if title[1] <10: pass
        es.add('',data.keys().data.values())
        flag += 1
    es.render()
    es.render()
if __name__ == '__main__':
    data = {'成都':78,'上海':304,'深圳':194,
            '大连':27,'北京':200,'重庆':21,
            '杭州':75,'广州':108,'南京':58,
            '武汉':71,'长沙':28,'苏州':25,
            '合肥':15,'沈阳':14,'西安':36,
            '无锡':11,'郑州':16,'宁波':10,
            '福州':12,'天津':12}
    demoa(data)







