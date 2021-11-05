#!/usr/bin/python3
from kafka import KafkaConsumer
import json
import csv
import os
import time

consumer = KafkaConsumer('jxrs',  bootstrap_servers=['192.168.10.72:9192'], auto_offset_reset='earliest')
for msg in consumer:
    msg = msg.value.decode('utf-8')
    try:
        dic = json.loads(msg)
    except Exception as e:
        print(e)
        print(msg)
        continue
    v_app = []
    v_business = []
    v_ip = []
    v_message = []
    v_log = []
    v_timestamp = []
    v_nanos = []
    i = 0
    long = len(dic)
    for key, value in dic.items():
        i += 1
        if key == 'app':
            v_app.append(value)
        elif key == 'business':
            v_business.append(value)
        elif key == 'host':
            v_ip.append(value)
        elif key == 'message':
            v_message.append(value)
        elif key == 'log_file_path':
            v_log.append(value)
        elif key == 'timestamp_nanos':
            values = int(value)
            dat = round(values//1000000000)
            v_timestamp.append(dat)
            v_nanos.append(value)
        if i == long:
            if len(v_app) and len(v_business) and len(v_ip) and len(v_log) and len(v_timestamp) and len(v_message):
                tupTime = time.localtime(v_timestamp[0])
                dt = time.strftime("%Y-%m-%d", tupTime)
                # ds = time.strftime('%H', tupTime)
                ctlog = '/home/ap/ailog/log_storage/' + v_business[0] + '/' + v_app[0] + '/' + v_ip[0] + '/' + v_log[0] + '/' + dt
                if not os.path.isdir(ctlog):
                    os.makedirs(ctlog)
                f = ctlog + '/' + dt + r'.csv'
                if not os.path.isfile(f):
                    fl = open(f, 'a', encoding='utf-8', newline="")
                    csv_writer = csv.writer(fl)
                    csv_writer.writerow(['message', 'times'])
                else:
                    fl = open(f, 'a', encoding='utf-8', newline="")
                    csv_writer = csv.writer(fl)
                csv_writer.writerow([v_message[0], v_nanos[0]])
                fl.close()
            else:
                print("某行缺少元素")
