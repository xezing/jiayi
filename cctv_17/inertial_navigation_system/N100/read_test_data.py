#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import math

"""
读取采集到的数据文件，并拿出其中的xyz加速度数据并计算出当前速度
将当前速度与时间相乘并存入里程变量中
"""


class N100:
    Vt = 0
    distance = 0

    # 读取数据文件
    # todo 根据时间范围读取相应的数据
    def readData(self, filePath):
        vt = 0
        distance = 0

        with open(filePath, 'r') as fp:
            sec = -1
            count = 0
            for line in fp.readlines():
                line_split = line.split(',')

                # 首先筛选出40协议的数据
                if (line_split[1].strip() == '40'):
                    time = line_split[0]
                    time_split = time.split(" ")
                    timestamp = time_split[1].split(":")
                    second = timestamp[2][0:2]
                    if(second != sec):
                        sec = second
                        if (count != 0):
                            vt = vt/count * 36
                            print(vt)
                        count = 0
                        vt = 0
                    else:
                        count = count + 1
                        # print(count)

                    acc_x = float(line_split[5])
                    acc_y = float(line_split[6])
                    acc_z = float(line_split[7])
                    # 如果x轴加速度为负值则初速度需减去加速度，若为正值则加上初速度
                    # print(math.cos(math.atan(acc_x / math.sqrt(acc_y * acc_y + acc_z * acc_z))) * 9.8)
                    # print(math.cos(math.atan(acc_y / math.sqrt(acc_x * acc_x + acc_z * acc_z))) * 9.8)
                    # print(math.cos(math.atan(acc_z / math.sqrt(acc_x * acc_x + acc_y * acc_y))) * 9.8)
                    if (acc_x < 0):
                        vt = vt - math.sqrt(acc_x * acc_x + acc_y * acc_y)
                        distance = distance + vt
                        # print(time, "       ", vt * 3.6, "           ", distance)
                        # print(math.sqrt(acc_x * acc_x + acc_y * acc_y))
                    else:
                        vt = vt + math.sqrt(acc_x * acc_x + acc_y * acc_y)
                        distance = distance + vt
                        # print(time, "       ", vt * 3.6, "         ", distance)
                        # print(math.sqrt(acc_x * acc_x + acc_y * acc_y))


if __name__ == '__main__':
    filePath = r'../../inertial_navigation_system/data_source/result_20211027.txt'
    n100 = N100()
    n100.readData(filePath)
