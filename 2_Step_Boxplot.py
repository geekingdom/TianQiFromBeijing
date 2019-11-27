#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
作者：Zhixing Tu

时间：2019/11/27  10:17 上午

文件：2_Step_Boxplot.py

IDE：PyCharm
'''

import pandas as pd
from pyecharts import Boxplot

dic = {"Aotizhongxin": "奥体中心", "Changping": "昌平", "Dingling": "定陵", "Dongsi": "东四", "Guanyuan": "官园",
       "Gucheng": "古城", "Huairou": "怀柔", "Nongzhanguan": "农展馆", "Shunyi": "顺义", "Tiantan": "天坛", "Wanliu": "万柳",
       "Wanshouxigong": "万寿西宫"}

def Seasion(city,year,key_word):
    df = pd.read_csv('./data/' + city + '/' + city + '_' + year + '.csv', header=None,
                     names=["Date", "PM25", "PM10", "SO2", "NO2", "CO", "O3"])

    dom = df[['Date', key_word]]
    data = [[], [], [], []]
    dom1, dom2, dom3, dom4 = data
    for i, j in zip(dom['Date'], dom[key_word]):
        time = i.split('-')[1]
        if time in ['1', '2', '3']:
            dom1.append(j)
        elif time in ['4', '5', '6']:
            dom2.append(j)
        elif time in ['7', '8', '9']:
            dom3.append(j)
        else:
            dom4.append(j)

    boxplot = Boxplot(year+"年"+dic[city]+"季度"+key_word+"箱形图", title_pos='center', title_top='18', width=800, height=400)
    x_axis = ['第一季度', '第二季度', '第三季度', '第四季度']
    y_axis = [dom1, dom2, dom3, dom4]
    _yaxis = boxplot.prepare_data(y_axis)
    boxplot.add("", x_axis, _yaxis)
    boxplot.render("./assets/"+city+"/" + key_word + "/" + year + "/" +year+"年"+dic[city]+key_word+"季度箱形图.html")


if __name__ == '__main__':
    Cities = ["Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan",
              "Gucheng", "Huairou", "Nongzhanguan", "Shunyi", "Tiantan", "Wanliu", "Wanshouxigong"]
    years = ['2013', '2014', '2015', '2016', '2017']
    keys = ["PM25", "PM10", "SO2", "NO2", "CO", "O3"]
    for c in Cities:
        for y in years:
            for k in keys:
                Seasion(str(c), str(y), str(k))