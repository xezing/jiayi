#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import math
import datetime
from pykafka import KafkaClient

"""
读取采集到的数据文件，并将数据存入kafka的topic中
"""

host = 'jiayiai.wicp.vip'
client = KafkaClient(hosts="%s:29092" % host)
print(client.topics)

# 消费者
topic = client.topics['n100_1216']

def dumpData(filePath):
    with open(filePath, 'r') as fp:
        with topic.get_sync_producer() as producer:
    # with topic.get_sync_producer() as producer:
        # with open(filePath, 'r') as fp:
            for line in fp.readlines():
                try:
                    m_split = line.split(',')
                    # 首先筛选出40协议的数据
                    if (m_split[1].strip() == '40'):
                        gyroscope_x = m_split[2].strip()
                        gyroscope_y = m_split[3].strip()
                        gyroscope_z = m_split[4].strip()
                        accelerometer_x = m_split[5].strip()
                        accelerometer_y = m_split[6].strip()
                        accelerometer_z = m_split[7].strip()
                        magnetometer_x = m_split[8].strip()
                        magnetometer_y = m_split[9].strip()
                        magnetometer_z = m_split[10].strip()
                        imu_temperature = m_split[11].strip()
                        pressure = m_split[12].strip()
                        pressure_temperature = m_split[13].strip()
                        timestamp = m_split[0].strip()

                        output = str(gyroscope_x) + "," + str(gyroscope_y) + "," + str(gyroscope_z) + "," + str(
                            accelerometer_x) + "," + str(accelerometer_y) + "," + str(accelerometer_z) + "," + str(
                            magnetometer_x) + "," + str(magnetometer_y) + "," + str(magnetometer_z) + "," + str(
                            imu_temperature) + "," + str(pressure) + "," + str(pressure_temperature) + "," + str(
                            timestamp)
                        print(output)
                        producer.produce(bytes(output, encoding='utf-8'))
                except Exception as e:
                    print(e)



    # 时间转换

def trans_time(self, time):
        full_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
        add_time = (full_time + datetime.timedelta(seconds=40))
        new_time = add_time.strftime("%Y-%m-%d %H:%M:%S.%f")
        return new_time





if __name__ == '__main__':
    filePath = r'C:\Users\Admin\Desktop\result_20211216.txt'
    dumpData(filePath)