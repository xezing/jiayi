#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from pykafka import KafkaClient
import pymysql

"""
1、从kafka读取数据，并得到日期信息
2、数据库连接
3、查询数据库中是否存在表ins_n100_date
4、存在则插入，不存在则创建并插入
"""


# 创建数据库连接
def get_con():
    config = {
        "host": "192.168.10.32",
        "port": 3308,
        "user": "cbtc",
        "password": "cbtc#456",
        "database": "cbtc"
    }
    db = pymysql.connect(**config)
    cursor = db.cursor()
    return cursor


# 查询数据库中是否存在表
def exist_table(cur):
    execute = cur.execute("select count(1) from information_schema.tables where table_name ='student';")
    result = [tuple[0] for tuple in cur.fetchall()]
    return result


if __name__ == '__main__':
    cur = get_con()
    print(exist_table(cur)[0])
