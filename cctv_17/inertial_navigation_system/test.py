# -*- encoding: utf-8 -*-
import math

"""
测试计算
"""
filePath = r'D:\workspace\jiayi\cctv_17\inertial_navigation_system\data_source\time_table_01.txt'
with open(filePath, 'r') as fp:
    distance = 0
    v0 = 0
    for line in fp.readlines():
        # print(len(line))
        if (len(line) > 5):
            line_split = line.split(",")
            vt = float(line_split[1])
            distance = distance + vt*5/18
            # print(vt)
            a = (vt - v0) * 5 / 18
            v0 = vt
            print(a, distance)

