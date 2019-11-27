#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
作者：Zhixing Tu

时间：2019/11/27  10:12 上午

文件：2_Step_Pie.py

IDE：PyCharm
'''

import pandas as pd
from pyecharts import Bar, Scatter3D,Page

df = pd.read_csv('air_tianjin_2017.csv', header=None, names=["Date", "Quality_grade", "AQI", "AQI_rank", "PM"])

rank_message = df.groupby(['Quality_grade'])
rank_com = rank_message['Quality_grade'].agg(['count'])
rank_com.reset_index(inplace=True)
rank_com_last = rank_com.sort_values('count', ascending=False)

attr = rank_com_last['Quality_grade']
v1 = rank_com_last['count']

pie = Pie("2017年天津全年空气质量情况", title_pos='center', title_top=0)
pie.add("", attr, v1, radius=[40, 75], label_text_color=None, is_label_show=True, legend_orient="vertical", legend_pos="left", legend_top="%10")
pie.render('2017年天津全年空气质量情况.html')


page = Page()# st
attr = ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
attr = ["PM25", "PM10", "SO2", "NO2", "CO", "O3"]
v1 = [5,20,36,10,75,90]
v2 = [10,25,8,60,20,80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1,is_stack=True,mark_point=['average'])
bar.add("商家B", attr, v2,is_stack=True,is_convert=True) #对图表进行转置
page.add(bar)# step 2
page.render()# step 3