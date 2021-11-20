#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import math
import datetime
from pykafka import KafkaClient


"""
从kafka读取采集到的数据文件，并拿出其中的xyz加速度数据并计算出当前速度
将当前速度与时间相乘并存入里程变量中
"""

# 时间转换
def trans_time(time):
    full_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
    add_time = (full_time + datetime.timedelta(seconds=40))
    new_time = add_time.strftime("%Y-%m-%d %H:%M:%S.%f")
    return new_time

host = 'jiayiai.wicp.vip'
def cal_distance(start_time):
    try:
        vt = 0
        distance = 0
        ax = 0
        sec = -1
        count = 0

        client = KafkaClient(hosts="%s:29092" % host)
        topic = client.topics['gps']
        consumer = topic.get_simple_consumer(consumer_group='gps', auto_commit_enable=True, consumer_id='gps')

        for message in consumer:
            m = str(message.value.decode('utf-8'))
            m_split = m.split(',')
            # print(message.offset, message.value)
            gyroscope_x = m_split[0]
            gyroscope_y = m_split[1]
            gyroscope_z = m_split[2]
            accelerometer_x = m_split[3]
            accelerometer_y = m_split[4]
            accelerometer_z = m_split[5]
            magnetometer_x = m_split[6]
            magnetometer_y = m_split[7]
            magnetometer_z = m_split[8]
            imu_temperature = m_split[9]
            pressure = m_split[10]
            pressure_temperature = m_split[11]
            timestamp = m_split[12]

            time = trans_time(m_split[12])
            check_time = time[0:-7]
            time_split = time.split(" ")
            times = time_split[1].split(":")
            second = times[2][0:2]
            acc_x = float(m_split[3]) - 0.04
            acc_y = float(m_split[4])
            acc_z = float(m_split[5])
            acc = math.sqrt(acc_x * acc_x + acc_y * acc_y + acc_z * acc_z)
            if(acc>100):
                continue
                # print(time, acc_x, acc_y, acc_z, acc)
                # 平均后的数据
            if (second != sec):
                sec = second
                if (count != 0):
                    ax = ax/(count+1)
                    # if (ax < 0.005 and ax > 0):
                    #     ax = 0
                    vt = vt + ax
                    if (vt < -1 ):
                        vt = 0
                    distance = distance + vt
                    # print(time, ',', distance)
                    print(time,"   ax =", ax,"    vt =",  vt*3.6, "    distance=",distance)
                    # print(time,ax)
                    # print(vt*3.6)
                count = 0
                # vt = 0
            else:
                count = count + 1
                ax = ax + acc_x
                # print(count)
    except Exception as e:
        print(e)
def get_ats():
    return 1
if __name__ == '__main__':
    if(get_ats() == 1):
        cal_distance()


