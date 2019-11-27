# TianQiFromBeijing

## Introduction | 项目简介

项目简介：对2013年3月至2017年2月北京市12个地点的空气监测数据进行分析处理。

数据来源：https://archive.ics.uci.edu/ml/datasets/Beijing+Multi-Site+Air-Quality+Data
数据简介：

Data Set Information:

```angular2
  This data set includes hourly air pollutants data from 12 nationally-controlled air-quality monitoring sites. The air-quality data are from the Beijing Municipal Environmental Monitoring Center. The meteorological data in each air-quality site are matched with the nearest weather station from the China Meteorological Administration. The time period is from March 1st, 2013 to February 28th, 2017. Missing data are denoted as NA.
```

Attribute Information:

```angular2
    No: row number
    year: year of data in this row
    month: month of data in this row
    day: day of data in this row
    hour: hour of data in this row
    PM2.5: PM2.5 concentration (ug/m^3)
    PM10: PM10 concentration (ug/m^3)
    SO2: SO2 concentration (ug/m^3)
    NO2: NO2 concentration (ug/m^3)
    CO: CO concentration (ug/m^3)
    O3: O3 concentration (ug/m^3)
    TEMP: temperature (degree Celsius)
    PRES: pressure (hPa)
    DEWP: dew point temperature (degree Celsius)
    RAIN: precipitation (mm)
    wd: wind direction
    WSPM: wind speed (m/s)
    station: name of the air-quality monitoring site
```

## Download | 项目下载

```bash
$ git clone https://github.com/geekingdom/TianQiFromBeijing.git
$ cd TianQiFromBeijing
```

## Requirements

- python==3.7.4
- pandas==0.25.1
- csv==1.0
- pyecharts==0.5.5

## Details | 项目流程简介

### 1. 下载源数据集

- 将下载的数据集进行重命名简化并拷贝至项目```data```文件夹下，如下图：
- ![img](./aimages/ShortCut_1.png)
- 部分源数据展示
  ```angular2
    "No","year","month","day","hour","PM2.5","PM10","SO2","NO2","CO","O3","TEMP","PRES","DEWP","RAIN","wd","WSPM","station"
    1,2013,3,1,0,4,4,4,7,300,77,-0.7,1023,-18.8,0,"NNW",4.4,"Aotizhongxin"
    2,2013,3,1,1,8,8,4,7,300,77,-1.1,1023.2,-18.2,0,"N",4.7,"Aotizhongxin"
    3,2013,3,1,2,7,7,5,10,300,73,-1.1,1023.5,-18.2,0,"NNW",5.6,"Aotizhongxin"
    4,2013,3,1,3,6,6,11,11,300,72,-1.4,1024.5,-19.4,0,"NW",3.1,"Aotizhongxin"
    5,2013,3,1,4,3,3,12,12,300,72,-2,1025.2,-19.5,0,"N",2,"Aotizhongxin"
    6,2013,3,1,5,5,5,18,18,400,66,-2.2,1025.6,-19.6,0,"N",3.7,"Aotizhongxin"
    7,2013,3,1,6,3,3,18,32,500,50,-2.6,1026.5,-19.1,0,"NNE",2.5,"Aotizhongxin"
    8,2013,3,1,7,3,6,19,41,500,43,-1.6,1027.4,-19.1,0,"NNW",3.8,"Aotizhongxin"
    9,2013,3,1,8,3,6,16,43,500,45,0.1,1028.3,-19.2,0,"NNW",4.1,"Aotizhongxin"
    10,2013,3,1,9,3,8,12,28,400,59,1.2,1028.5,-19.3,0,"N",2.6,"Aotizhongxin"
    11,2013,3,1,10,3,6,9,12,400,72,1.9,1028.2,-19.4,0,"NNW",3.6,"Aotizhongxin"
    12,2013,3,1,11,3,6,9,14,400,71,2.9,1028.2,-20.5,0,"N",3.7,"Aotizhongxin"
    13,2013,3,1,12,3,6,7,13,300,74,3.9,1027.3,-19.7,0,"NNW",5.1,"Aotizhongxin"
    14,2013,3,1,13,3,6,7,12,400,76,5.3,1026.2,-19.3,0,"NW",4.3,"Aotizhongxin"
    15,2013,3,1,14,6,9,7,11,400,77,6,1025.9,-19.6,0,"NW",4.4,"Aotizhongxin"
    16,2013,3,1,15,8,15,7,14,400,76,6.2,1025.7,-18.6,0,"NNE",2.8,"Aotizhongxin"
    17,2013,3,1,16,9,19,9,13,400,76,5.9,1025.6,-18.1,0,"NNW",3.9,"Aotizhongxin"
  ```

### 2. 利用csv对源数据集数据进行处理

-将源数据集中的数据按照年份分开

-将源数据集中的数据的日期列进行合并且改格式为```年-月-日```

-将每日24小时的数据求和取均值存入对应的日期

-在```data```文件夹中按照源数据集中的地点创建相应文件夹，并把处理后的数据按照地点和年份存入对应文件夹
  
  ```python
     with open('./data/' + filename + '/' + filename + '_' + str(year) + '.csv', 'a+',
          encoding='utf-8-sig') as f:
          f.write(Date + ',' + str(PM25) + ',' + str(PM10) + ',' + str(SO2) + ',' + str(NO2) + ',' + str(
                 CO) + ',' + str(O3) + '\n')
  ```
 -处理后```data```目录下文件如图所示
 - ![img](./aimages/ShortCut_2.png)
 
 -部分处理后的数据展示
 ```angular2
    2013-3-1,7,11,12,23,429,64
    2013-3-2,31,42,37,67,825,30
    2013-3-3,77,121,61,81,1621,19
    2013-3-4,23,45,22,45,592,54
    2013-3-5,149,184,94,133,2358,68
    2013-3-6,223,265,116,142,2979,20
    2013-3-7,263,316,98,148,3633,39
    2013-3-8,221,298,66,114,2366,79
    2013-3-9,62,202,33,45,1179,74
    2013-3-10,34,69,23,50,708,83
    2013-3-11,124,178,87,91,1671,75
    2013-3-12,123,117,28,73,1567,37
    2013-3-13,16,19,16,36,504,72
    2013-3-14,95,107,52,70,1337,69
    2013-3-15,212,251,76,99,2116,44
    2013-3-16,245,258,70,90,2083,67
    2013-3-17,285,310,74,114,2558,97
    2013-3-18,71,118,20,46,867,89
    2013-3-19,41,49,16,49,567,18
    2013-3-20,49,48,12,42,921,32
  ```
  
### 3. 利用pandas和pyecharts对数据进行可视化

## Author

- Zhixing TU @2019-11-27
