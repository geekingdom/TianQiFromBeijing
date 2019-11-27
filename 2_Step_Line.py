#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
作者：Zhixing Tu

时间：2019/11/26  8:22 下午

文件：2_Step_Line.py

IDE：PyCharm
'''

import numpy as np
import pandas as pd
from pyecharts import Line

dic = {"Aotizhongxin": "奥体中心", "Changping": "昌平", "Dingling": "定陵", "Dongsi": "东四", "Guanyuan": "官园",
       "Gucheng": "古城", "Huairou": "怀柔", "Nongzhanguan": "农展馆", "Shunyi": "顺义", "Tiantan": "天坛", "Wanliu": "万柳",
       "Wanshouxigong": "万寿西宫"}


def Fullyear(city, year, key_word):
    df = pd.read_csv('./data/' + city + '/' + city + '_' + year + '.csv', header=None,
                     names=["Date", "PM25", "PM10", "SO2", "NO2", "CO", "O3"])
    attr = df['Date']
    v1 = df[key_word]
    line = Line(year + dic[city] + key_word + "全年走势图", title_pos='center', title_top='18', width=800, height=400)
    line.add("", attr, v1, mark_line=['average'], is_fill=True, area_color="#000", area_opacity=0.3,
             mark_point=["max", "min"], mark_point_symbol="circle", mark_point_symbolsize=25)
    line.render("./assets/"+city+"/" + key_word + "/" + year + "/" + year + "年"+dic[city]+ key_word + "全年走势图.html")


def EveryMonth(city, year, key_word):
    df = pd.read_csv('./data/' + city + '/' + city + '_' + year + '.csv', header=None,
                     names=["Date", "PM25", "PM10", "SO2", "NO2", "CO", "O3"])

    dom = df[['Date', key_word]]
    list1 = []
    for j in dom['Date']:
        time = j.split('-')[1]
        list1.append(time)
    df['month'] = list1

    month_message = df.groupby(['month'])
    month_com = month_message[key_word].agg(['mean'])
    month_com.reset_index(inplace=True)
    month_com_last = month_com.sort_index()
    if year == '2013':
        attr = ["{}".format(str(i) + '月') for i in range(3, 13)]
    elif year == '2017':
        attr = ["{}".format(str(i) + '月') for i in range(1, 3)]
    else:
        attr = ["{}".format(str(i) + '月') for i in range(1, 13)]
    v1 = np.array(month_com_last['mean'])
    v1 = ["{}".format(int(i)) for i in v1]

    line = Line(year + "年"+dic[city]+"月均" + key_word + "走势图", title_pos='center', title_top='18', width=800, height=400)
    line.add("", attr, v1, mark_point=["max", "min"])
    line.render("./assets/"+city+"/" + key_word + "/" + year + "/" + year + "年"+dic[city]+"月均" + key_word + "走势图.html")


if __name__ == '__main__':
    Cities = ["Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan",
              "Gucheng", "Huairou", "Nongzhanguan", "Shunyi", "Tiantan", "Wanliu", "Wanshouxigong"]
    years = ['2013', '2014', '2015', '2016', '2017']
    keys = ["PM25", "PM10", "SO2", "NO2", "CO", "O3"]
    for c in Cities:
        for y in years:
            for k in keys:
                Fullyear(str(c), str(y), str(k))
    for c in Cities:
        for y in years:
            for k in keys:
                EveryMonth(str(c), str(y), str(k))
