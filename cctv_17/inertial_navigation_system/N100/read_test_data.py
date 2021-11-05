#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import math
import datetime

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
        with open(filePath, 'r') as fp:
            vt = 0
            distance = 0
            ax = 0
            sec = -1
            count = 0
            for line in fp.readlines():
                line_split = line.split(',')

                # 首先筛选出40协议的数据
                if (line_split[1].strip() == '40'):
                    time = self.trans_time(line_split[0])


                    time_split = time.split(" ")
                    timestamp = time_split[1].split(":")
                    second = timestamp[2][0:2]

                    acc_x = float(line_split[5]) - 0.06
                    acc_y = float(line_split[6])
                    acc_z = float(line_split[7])
                    acc = math.sqrt(acc_x * acc_x + acc_y * acc_y + acc_z * acc_z)

                    if(acc>100):
                        continue
                    # print(time, acc_x, acc_y, acc_z, acc)
                    # #平滑后的数据
                    if (second != sec):
                        sec = second
                        if (count != 0):
                            ax = ax/count
                            vt = vt + ax
                            if (vt < 0 ):
                                vt = 0
                            distance = distance + vt
                            print(time, ax, vt*3.6, vt, distance)

                        count = 0
                        # vt = 0
                    else:
                        count = count + 1
                        ax = ax + acc_x
                        # print(count)

    # 时间转换
    def trans_time(self, time):
        full_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
        add_time = (full_time + datetime.timedelta(seconds=40))
        new_time = add_time.strftime("%Y-%m-%d %H:%M:%S.%f")
        return new_time


if __name__ == '__main__':
    filePath = r'D:\workspace\jiayi\cctv_17\inertial_navigation_system\data_source\1103_01.txt'
    n100 = N100()
    n100.readData(filePath)