#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import datetime
import mysql_pool

"""
1、从kafka读取数据，并得到日期信息
2、数据库连接
3、查询数据库中是否存在表ins_n100_date
4、存在则插入，不存在则创建并插入
"""

if __name__ == '__main__':
    pool = mysql_pool.ConnMysql()
    cursor = pool.cur
    db = pool.coon

    datetime_now = datetime.datetime.now()
    date_time = datetime_now.strftime('%Y-%m-%d')
    create_sql = '''CREATE TABLE `ins_n100_imu_%s` (\
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
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;''' % date_time

    sql = "select count(1) from information_schema.tables where table_name ='ins_n100_imu_%s';" % date_time
    result = pool.sql_select_many(sql)[0].get('count(1)')

    if result == 0:
        cursor.execute(create_sql)
        db.commit()
    cursor.close()
    db.close()
