# -*- coding=utf8 -*-
__author__ = 'admin'

def chooise_xifu():

    age_list = [18,19,20,21,22,23,66,70]
    luck_age = int(input("你想要的年龄(18-50) :"))
    for age in age_list:

        if  luck_age > 17 and luck_age < 50:

            print("okay,恭喜%s:都可以选择 "%(age))
        elif luck_age < 18:
            print("太小了")

        else:
            print("治生不求富,读书不求官,修德不求报,为文不求传,譬如饮酒不醉,陶然有余欢,中含不尽意,欲辨已忘言。")

chooise_xifu()
