#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from pykafka import KafkaClient
import pymysql

config = {
    "host": "192.168.10.32",
    "port": 3308,
    "user": "cbtc",
    "password": "cbtc#456",
    "database": "cbtc"
}
db = pymysql.connect(**config)
cursor = db.cursor()
# 使用execute()方法执行SQL语句
# cursor.execute("select * from rpt_time_table")
# 使用fetall()获取全部数据
# data = cursor.fetchall()
# 打印获取到的数据
# print(data)

host = 'jiayiai.wicp.vip'
client = KafkaClient(hosts="%s:29092" % host)
print(client.topics)

# 消费者
topic = client.topics['gps']
consumer = topic.get_simple_consumer(consumer_group='gps', auto_commit_enable=True, consumer_id='gps')
for message in consumer:
    if message is not None:
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

        sql1 = "INSERT INTO ins_n100_imu(gyroscope_x,gyroscope_y,gyroscope_z,accelerometer_x,accelerometer_y,accelerometer_z,magnetometer_x,magnetometer_y,magnetometer_z,imu_temperature,pressure,pressure_temperature,timestamp) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            gyroscope_x, gyroscope_y, gyroscope_z, accelerometer_x, accelerometer_y, accelerometer_z,
            magnetometer_x, magnetometer_y, magnetometer_z, imu_temperature, pressure, pressure_temperature,
            timestamp)
        sql2 = "INSERT INTO ins_n100_imu_history(gyroscope_x, gyroscope_y, gyroscope_z, accelerometer_x, accelerometer_y, accelerometer_z, magnetometer_x, magnetometer_y, magnetometer_z, imu_temperature, pressure, pressure_temperature, timestamp) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            gyroscope_x, gyroscope_y, gyroscope_z, accelerometer_x, accelerometer_y, accelerometer_z,
            magnetometer_x, magnetometer_y, magnetometer_z, imu_temperature, pressure, pressure_temperature,
            timestamp)

        cursor.execute(sql1)
        cursor.execute(sql2)
        db.commit()  # 提交数据

cursor.close()
db.close()
