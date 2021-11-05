#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import serial
import os
import sys
import time, datetime
from datetime import datetime
from time import sleep
from optparse import OptionParser
import struct
from pykafka import KafkaClient

"""
此脚本可将N100串口数据解析，其中包括0X40 0X41 0X6F三种不同通信协议的内容
并将解析好的数据发送到kafka的gps topic下
"""

def secs2str(secs):
    s = "%.3f" % secs
    ms = s.split(".")[1]
    return time.strftime("%Y-%m-%d %H:%M:%S." + ms, time.localtime(secs))


def getCurrentDateTime():
    secs = time.time()
    return secs2str(secs)


def getDateTime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")


def writefile(filename, lines):
    out = file(filename, 'w')
    for line in lines:
        out.write('%s' % line)
    out.close()


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-d', '--device', help="usb device")
    opts, args = parser.parse_args()

    if not opts.device:
        parser.error('device is required!')

    scanTime = getCurrentDateTime()
    print("scan time: %s" % (scanTime))

    ser = serial.Serial(opts.device, 115200, timeout=0.5)  # /dev/ttyUSB1
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

        output = ""
        bStart = False
        iNum = 0
        iCmd = 0
        sHeader = ""
        sBody = ""
        bHeader = False
        # raw_out = file("raw_file.txt", 'w')
        # result_out = file("result_file.txt", 'w')
        while True:
            try:
                x = ser.read(1)
                if not bStart:
                    if (ord(x) == 0xFC):
                        bHeader = True
                        bStart = True
                if bStart:
                    if iNum == 1:
                        iCmd = ord(x)
                        # print ('Cmd = %#X' % iCmd)
                    if iNum == 7:
                        bHeader = False
                    if bHeader:
                        sHeader = sHeader + x
                    else:
                        sBody = sBody + x
                    # print ('%#X' % ord(x)),
                    # raw_out.write('%#X,' % ord(x))
                iNum = iNum + 1
                if (ord(x) == 0xFD):
                    # print ("")
                    # raw_out.write('\n')
                    try:
                        if (iCmd == 0x40):
                            header_start, data_type, data_size, serial_num, header_crc8, header_crc16_h, header_crc16_l = struct.unpack(
                                "!7B", sHeader)
                            # print ('header length = %d, body length = %d, %X, %X, %d, %d' %(len (sHeader), len (sBody), header_start, data_type, data_size, serial_num))
                            gyroscope_x, gyroscope_y, gyroscope_z, accelerometer_x, accelerometer_y, accelerometer_z, magnetometer_x, magnetometer_y, magnetometer_z, imu_temperature, pressure, pressure_temperature, timestamp, body_end = struct.unpack(
                                "<12fQB", sBody)
                            print('%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %d' % (
                                gyroscope_x, gyroscope_y, gyroscope_z, accelerometer_x, accelerometer_y,
                                accelerometer_z,
                                magnetometer_x, magnetometer_y, magnetometer_z, imu_temperature, pressure,
                                pressure_temperature,
                                timestamp))
                            # result_out.write('%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %d\n' % (
                            # gyroscope_x, gyroscope_y, gyroscope_z, accelerometer_x, accelerometer_y, accelerometer_z,
                            # magnetometer_x, magnetometer_y, magnetometer_z, imu_temperature, pressure, pressure_temperature,
                            # timestamp))
                            output = str(gyroscope_x) + "," + str(gyroscope_y) + "," + str(gyroscope_z) + "," + str(
                                accelerometer_x) + "," + str(accelerometer_y) + "," + str(accelerometer_z) + "," + str(
                                magnetometer_x) + "," + str(magnetometer_y) + "," + str(magnetometer_z) + "," + str(
                                imu_temperature) + "," + str(pressure) + "," + str(pressure_temperature) + "," + str(
                                timestamp)
                            print(output)
                            producer.produce(bytes(output).encode('utf-8'))
                        elif (iCmd == 0x6F):
                            header_start, data_type, data_size, serial_num, header_crc8, header_crc16_h, header_crc16_l = struct.unpack(
                                "!7B", sHeader)
                            odom_count, odom_distance, odom_speed, odom_slip, odom_active, reserved, body_end = struct.unpack(
                                "<i3f2IB", sBody)
                    except Exception as ex:
                        print('[%s] : Header Length = [%d], Body Length = [%d], Exception : [%s].' % (
                            getDateTime(), len(sHeader), len(sBody), ex))
                        # print (sBody)
                    iNum = 0
                    bStart = False
                    sHeader = ""
                    sBody = ""

                sys.stdout.flush()
                producer.produce(bytes(output).encode('utf-8'))
                # print('Recv Info : %#X' %(strInfo))
            except Exception as ex:
                print('Cause Exception : %s' % (ex))
                # raw_out.close()
                # result_out.close()
                ser.close()
                sys.exit(0)
    ser.close()
