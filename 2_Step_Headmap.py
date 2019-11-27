#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
作者：Zhixing Tu

时间：2019/11/27  10:17 上午

文件：2_Step_Headmap.py

IDE：PyCharm
'''

import datetime
import numpy as np
import pandas as pd
from pyecharts import HeatMap

dic = {"Aotizhongxin": "奥体中心", "Changping": "昌平", "Dingling": "定陵", "Dongsi": "东四", "Guanyuan": "官园",
       "Gucheng": "古城", "Huairou": "怀柔", "Nongzhanguan": "农展馆", "Shunyi": "顺义", "Tiantan": "天坛", "Wanliu": "万柳",
       "Wanshouxigong": "万寿西宫"}

size = {"PM25":400, "PM10":500, "SO2":100, "NO2":200, "CO":8000, "O3":200}

def Fullyear(city,year,key_word):
    df = pd.read_csv('./data/' + city + '/' + city + '_' + year + '.csv', header=None,
                     names=["Date", "PM25", "PM10", "SO2", "NO2", "CO", "O3"])
    v1 = ["{}".format(int(i)) for i in np.array(df[key_word])]
    if year == "2013":
        begin = datetime.date(int(year), 3, 1)
        end = datetime.date(int(year), 12, 31)
    elif year == "2017":
        begin = datetime.date(int(year), 1, 1)
        end = datetime.date(int(year), 2, 27)
    else:
        begin = datetime.date(int(year), 1, 1)
        end = datetime.date(int(year), 12, 31)

    data = [[str(begin + datetime.timedelta(days=i)), v1[i]] for i in range((end - begin).days + 1)]
    heatmap = HeatMap(year+"年"+dic[city]+key_word+"指数日历图", title_pos='40%', title_top='10', width=800, height=400)
    heatmap.add(
        "",
        data,
        is_calendar_heatmap=True,
        visual_text_color="#000",
        visual_range_text=["", ""],
        visual_range=[0, size[key_word]],
        calendar_cell_size=["auto", 30],
        is_visualmap=True,
        calendar_date_range=year,
        visual_orient="horizontal",
        visual_pos="10%",
        visual_top="70%",
        is_piecewise=True,
        visual_split_number=6,
    )
    heatmap.render("./assets/"+city+"/" + key_word + "/" + year + "/" +year+'年'+dic[city]+key_word+'指数日历图.html')


if __name__ == '__main__':
    Cities = ["Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan",
              "Gucheng", "Huairou", "Nongzhanguan", "Shunyi", "Tiantan", "Wanliu", "Wanshouxigong"]
    years = ['2013', '2014', '2015', '2016', '2017']
    keys = ["PM25", "PM10", "SO2", "NO2", "CO", "O3"]
    for c in Cities:
        for y in years:
            for k in keys:
                Fullyear(str(c), str(y), str(k))