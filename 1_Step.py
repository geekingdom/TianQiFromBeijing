#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
作者：Zhixing Tu

时间：2019/11/25  10:49 下午

文件：1_Step.py

IDE：PyCharm
'''


import csv


def function(filename):
    with open('./data/PRSA_Data_' + filename + '.csv')as f:
        f_csv = csv.reader(f)
        ct = 0
        year = 0
        month = 0
        day = 1
        Date = ''
        PM25 = 0
        PM10 = 0
        SO2 = 0
        NO2 = 0
        CO = 0
        O3 = 0
        count = 0
        for row in f_csv:
            if ct == 0:
                ct = 1
                continue
            Day = int(row[3])
            if Day == day:
                count += 1
                a = row[5]
                b = row[6]
                c = row[7]
                d = row[8]
                e = row[9]
                f = row[10]
                if a == 'NA':
                    a = 0
                    PM25 += a
                else:
                    PM25 += round(float(a))
                if b == 'NA':
                    b = 0
                    PM10 += b
                else:
                    PM10 += round(float(b))
                if c == 'NA':
                    c = 0
                    SO2 += c
                else:
                    SO2 += round(float(c))
                if d == 'NA':
                    d = 0
                    NO2 += d
                else:
                    NO2 += round(float(d))
                if e == 'NA':
                    e = 0
                    CO += e
                else:
                    CO += round(float(e))
                if f == 'NA':
                    f = 0
                    O3 += f
                else:
                    O3 += round(float(f))
                year = int(row[1])
                month = int(row[2])
            else:
                PM25 = round(PM25 / count)
                PM10 = round(PM10 / count)
                SO2 = round(SO2 / count)
                NO2 = round(NO2 / count)
                CO = round(CO / count)
                O3 = round(O3 / count)
                Date = str(year) + "-" + str(month) + "-" + str(day)
                with open('./data/' + filename + '/' + filename + '_' + str(year) + '.csv', 'a+',
                          encoding='utf-8-sig') as f:
                    f.write(Date + ',' + str(PM25) + ',' + str(PM10) + ',' + str(SO2) + ',' + str(NO2) + ',' + str(
                        CO) + ',' + str(O3) + '\n')
                count = 1
                a = row[5]
                b = row[6]
                c = row[7]
                d = row[8]
                e = row[9]
                f = row[10]
                if a == 'NA':
                    a = 0
                    PM25 = a
                else:
                    PM25 = round(float(a))
                if b == 'NA':
                    b = 0
                    PM10 = b
                else:
                    PM10 = round(float(b))
                if c == 'NA':
                    c = 0
                    SO2 = c
                else:
                    SO2 = round(float(c))
                if d == 'NA':
                    d = 0
                    NO2 = d
                else:
                    NO2 = round(float(d))
                if e == 'NA':
                    e = 0
                    CO = e
                else:
                    CO = round(float(e))
                if f == 'NA':
                    f = 0
                    O3 = f
                else:
                    O3 = round(float(f))
                year = int(row[1])
                month = int(row[2])
                day = int(row[3])


if __name__ == '__main__':
    Cities = ["Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan",
              "Gucheng", "Huairou", "Nongzhanguan", "Shunyi", "Tiantan", "Wanliu", "Wanshouxigong"]
    for i in Cities:
        function(str(i))
