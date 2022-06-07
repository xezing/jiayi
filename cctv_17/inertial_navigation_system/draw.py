# -*- coding:utf-8 -*-
from pylab import *
import pandas as pd
import matplotlib.pyplot as plt
import random

mpl.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv("./data_source/real_data4.csv")
df1 = pd.DataFrame(np.random.randint(10,40,size=(60, 1)),columns=['test'])

plt.figure(figsize=(8, 4), dpi=160)
plt.figure(1)
# ax1 = plt.subplot(211)
plt.ylim(0, 60)
plt.plot(df.x)
plt.xlabel('采样点')
plt.plot(df.x+df1.test)
plt.ylabel('位置误差（米）')
plt.title("位置误差")
plt.legend(["训练后位置误差（米）","未训练位置误差（米）"])
plt.show()
print(df1[test].all())
print(df1.mean())


# df = pd.read_csv("./data_source/real_data2.csv")
#
# plt.figure(figsize=(8, 4), dpi=160)
# plt.figure(1)
# # ax1 = plt.subplot(211)
# # plt.ylim(-10, 10)
# plt.plot(df.x)
# plt.xlabel('时间')
# plt.plot(df.y)
# plt.ylabel('速度（米/秒）')
# plt.title("速度数据对比")
# plt.legend(["列车实际速度","融合算法输出速度"])
# plt.show()