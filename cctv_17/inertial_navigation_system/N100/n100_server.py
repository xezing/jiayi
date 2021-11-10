#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from pykafka import KafkaClient
import mysql_pool

host = 'jiayiai.wicp.vip'
client = KafkaClient(hosts="%s:29092" % host)
print(client.topics)

last_time = ""
# 消费者
topic = client.topics['gps']
consumer = topic.get_simple_consumer(consumer_group='gps', auto_commit_enable=True, consumer_id='gps')
try:
    pool = mysql_pool.ConnMysql()
    cursor = pool.cur
    db = pool.coon

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

            # 判断时间是否与预存储时间一致
            date = timestamp.split(" ")[0]
            date_time_split = date.split("-")
            date_time = date_time_split[0]+date_time_split[1]+date_time_split[2]
            # print(date_time)

            sql_insert = "INSERT INTO ins_n100_imu_%s(gyroscope_x,gyroscope_y,gyroscope_z,accelerometer_x,accelerometer_y,accelerometer_z,magnetometer_x,magnetometer_y,magnetometer_z,imu_temperature,pressure,pressure_temperature,timestamp) " \
                         "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
                         % (date_time, gyroscope_x, gyroscope_y, gyroscope_z, accelerometer_x, accelerometer_y,
                            accelerometer_z, magnetometer_x, magnetometer_y, magnetometer_z, imu_temperature, pressure,
                            pressure_temperature,
                            timestamp)
            sql_create = '''CREATE TABLE `ins_n100_imu_%s` (\
                    `gyroscope_x` varchar(255) DEFAULT NULL COMMENT '机体系X轴角速度',\
                    `gyroscope_y` varchar(255) DEFAULT NULL COMMENT '机体系Y轴角速度',\
                    `gyroscope_z` varchar(255) DEFAULT NULL COMMENT '机体系Z轴角速度',\
                    `accelerometer_x` varchar(255) DEFAULT NULL COMMENT '机体系X轴加速度(未分离重力加速度)',\
                    `accelerometer_y` varchar(255) DEFAULT NULL COMMENT '机体系Y轴加速度(未分离重力加速度)',\
                    `accelerometer_z` varchar(255) DEFAULT NULL COMMENT '机体系Z轴加速度(未分离重力加速度)',\
                    `magnetometer_x` varchar(255) DEFAULT NULL COMMENT '机体系X轴磁感应强度',\
                    `magnetometer_y` varchar(255) DEFAULT NULL COMMENT '机体系Y轴磁感应强度',\
                    `magnetometer_z` varchar(255) DEFAULT NULL COMMENT '机体系Z轴磁感应强度',\
                    `imu_temperature` varchar(255) DEFAULT NULL COMMENT 'IMU数据多个传感器的平均温度',\
                    `pressure` varchar(255) DEFAULT NULL COMMENT '气压值',\
                    `pressure_temperature` varchar(255) DEFAULT NULL COMMENT '气压计的温度值',\
                    `timestamp` varchar(255) DEFAULT NULL COMMENT '数据的时间戳'\
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;''' % (date_time)
            sql_check = "select count(1) from information_schema.tables where table_name ='ins_n100_imu_%s';" % (
                date_time)


            check_result = pool.sql_select_many(sql_check)[0].get('count(1)')
            if (check_result == 0):
                cursor.execute(sql_create)
                pool.sql_change_msg(sql_insert)
                db.commit()
            else:
                pool.sql_change_msg(sql_insert)
except Exception as e:
    print(str(e))
finally:
    pool.release()
