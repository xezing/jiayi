#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from pykafka import KafkaClient
import pymysql
config={
    "host":"192.168.10.32",
    "port":3308,
    "user":"cbtc",
    "password":"cbtc#456",
    "database":"cbtc"
}
db = pymysql.connect(**config)
cursor = db.cursor()
#使用execute()方法执行SQL语句
#cursor.execute("select * from rpt_time_table")
#使用fetall()获取全部数据
#data = cursor.fetchall()
#打印获取到的数据
#print(data)

host = 'jiayiai.wicp.vip'
client = KafkaClient(hosts="%s:29092" % host)
print(client.topics)


# 消费者
topic = client.topics['gps']
consumer = topic.get_simple_consumer(consumer_group='gps', auto_commit_enable=True, consumer_id='gps')
for message in consumer:
    if message is not None:
        print(message.offset, message.value)
        #sql = "INSERT INTO userinfo(username,passwd) VALUES('jack','123')"
        #cursor.execute(sql)
        #db.commit()  #提交数据
cursor.close()
db.close()
