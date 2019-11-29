#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
作者：Zhixing Tu

时间：2019/11/28  7:46 下午

文件：2_Step_Hedmap2.py

IDE：PyCharm
'''
import numpy as np
import pandas as pd
from pyecharts import Geo, Page, Style

data = {"Aotizhongxin": "朝阳区", "Changping": "昌平区", "Dingling": "昌平区", "Dongsi": "东城区", "Guanyuan": "西城区",
        "Gucheng": "石景山区", "Huairou": "怀柔区", "Nongzhanguan": "朝阳区", "Shunyi": "顺义区", "Tiantan": "东城区", "Wanliu": "海淀区",
        "Wanshouxigong": "西城区"}

size = {"PM25":400, "PM10":500, "SO2":100, "NO2":200, "CO":8000, "O3":200}

A_CYQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
A_CPQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
A_DCQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
A_XCQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
A_SJSQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
A_HRQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
A_SYQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
A_HDQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}


def Everyyear(year, key_word):
    page = Page()

    style = Style(
        title_color="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color="#404a59",
    )

    data = [('昌平区', A_CPQ[key_word]), ('怀柔区', A_HRQ[key_word]), ('西城区', A_XCQ[key_word]), ('东城区', A_DCQ[key_word]),
            ('顺义区', A_SYQ[key_word]), ('石景山区', A_SJSQ[key_word]), ('海淀区', A_HDQ[key_word]), ('朝阳区', A_CYQ[key_word])]
    chart = Geo(year+"北京市8个区的"+key_word+"热力图", **style.init_style)
    attr, value = chart.cast(data)
    chart.add("", attr, value, maptype="北京", type="heatmap", is_visualmap=True,
              is_legend_show=False,
              tooltip_formatter='{b}',
              label_emphasis_textsize=15,
              label_emphasis_pos='right',
              visual_range=[0, size[key_word]],
              visual_text_color="#fff"
              )
    page.add(chart)
    page.render("./assets/Beijing/" + year + "/" + year + "年北京市8个区的" + key_word + "热力图.html")


def Average(city, year, key_word):
    df = pd.read_csv('./data/' + city + '/' + city + '_' + year + '.csv', header=None,
                     names=["Date", "PM25", "PM10", "SO2", "NO2", "CO", "O3"])
    l1 = list(df[key_word])
    if city in ["Aotizhongxin", "Nongzhanguan"]:
        A_CYQ[key_word] += sum(l1) // l1.__len__()
        if city == "Nongzhanguan":
            A_CYQ[key_word] = A_CYQ[key_word] // 2
    if city in ["Changping", "Dingling"]:
        A_CPQ[key_word] += sum(l1) // l1.__len__()
        if city == "Dingling":
            A_CPQ[key_word] = A_CPQ[key_word] // 2
    if city in ["Dongsi", "Tiantan"]:
        A_DCQ[key_word] += sum(l1) // l1.__len__()
        if city == "Tiantan":
            A_DCQ[key_word] = A_DCQ[key_word] // 2
    if city in ["Guanyuan", "Wanshouxigong"]:
        A_XCQ[key_word] += sum(l1) // l1.__len__()
        if city == "Wanshouxigong":
            A_XCQ[key_word] = A_XCQ[key_word] // 2
    if city in ["Gucheng"]:
        A_SJSQ[key_word] += sum(l1) // l1.__len__()
    if city in ["Huairou"]:
        A_HRQ[key_word] += sum(l1) // l1.__len__()
    if city in ["Shunyi"]:
        A_SYQ[key_word] += sum(l1) // l1.__len__()
    if city in ["Wanliu"]:
        A_HDQ[key_word] += sum(l1) // l1.__len__()

def Reboot():
    A_CYQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
    A_CPQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
    A_DCQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
    A_XCQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
    A_SJSQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
    A_HRQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
    A_SYQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}
    A_HDQ = {"PM25": 0, "PM10": 0, "SO2": 0, "NO2": 0, "CO": 0, "O3": 0}

if __name__ == '__main__':
    cities = ["Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan",
              "Gucheng", "Huairou", "Nongzhanguan", "Shunyi", "Tiantan", "Wanliu", "Wanshouxigong"]
    years = ['2013', '2014', '2015', '2016', '2017']
    keys = ["PM25", "PM10", "SO2", "NO2", "CO", "O3"]
    for year in years:
        Reboot()
        for city in cities:
            for key in keys:
                Average(city,year,key)
        for key in keys:
            Everyyear(year,key)
