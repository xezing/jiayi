#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import serial
import os
import sys
# import redisUtil
import time, datetime
from time import sleep
from optparse import OptionParser
from pykafka import KafkaClient


def secs2str(secs):
    s = "%.3f" % secs
    ms = s.split(".")[1]
    return time.strftime("%Y-%m-%d %H:%M:%S." + ms, time.localtime(secs))


def getCurrentDateTime():
    secs = time.time()
    return secs2str(secs)


def calc_gps_pos(gps_info):
    gps_degree = int(float(gps_info) / 100)
    gps_cent = float(gps_info) - gps_degree * 100.0
    gps_value = gps_degree + gps_cent / 60.0
    return gps_value


def recv_msg(serial):
    msg = serial.read(1)
    sleep(0.3)
    msg = (msg + serial.read(serial.inWaiting())).decode()
    return msg


if __name__ == '__main__':
    parser = OptionParser()  #
    parser.add_option('-d', '--device', help="usb device")
    opts, args = parser.parse_args()

    if not opts.device:
        parser.error('device is required!')

    scanTime = getCurrentDateTime()
    print("scan time: %s" % (scanTime))

    ser = serial.Serial(opts.device, 9600, timeout=0.5)  # /dev/ttyUSB1
    if ser.isOpen():
        print("open [" + opts.device + "] success.")
    else:
        print("open [" + opts.device + "] failed.")
        exit()

    host = 'jiayiai.wicp.vip'
    client = KafkaClient(hosts="%s:29092" % host)
    print(client.topics)

    # 消费者
    displacement = 0
    topic = client.topics['gps']
    # 创建一个kafka生产者，这是一个同步生产者
    with topic.get_sync_producer() as producer:

        while True:
            try:
                strInfo = recv_msg(ser).splitlines()
                for strGps in strInfo:
                    if strGps.startswith('$'):
                        if strGps.startswith('$GPRMC') or strGps.startswith('$GNRMC'):
                            gpsFields = strGps.split(',')
                            status = gpsFields[2]
                            if (status == "A"):
                                latitude = calc_gps_pos(gpsFields[3])
                                longitude = calc_gps_pos(gpsFields[5])
                                scanTime = getCurrentDateTime()
                                speed = str(gpsFields[7])
                                displacement = int(gpsFields[7])*0.514 + displacement
                                cog = str(gpsFields[8])
                                gps = str(longitude) + "," + str(latitude) + "," + str(scanTime) + "," + speed + "," + cog + "," + str(displacement)
                                print("Time = " + scanTime + ", GPS = " + gps)
                                sys.stdout.flush()
                                # 将经纬度数据通过生产者发送到kafka的topic中
                                producer.produce(bytes(gps).encode('utf-8'))
            except Exception as ex:
                print('Cause Exception : %s' % (ex))
                ser.close()
                sys.exit(0)
        ser.close()
