#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from pykafka import KafkaClient

if __name__ == '__main__':

    strInfo = [[3.14, 2.12], [3.14, 2.12], [3.14, 2.12], [3.14, 2.12], [3.14, 2.12], [3.14, 2.12], [3.14, 2.12],
               [3.14, 2.12], [3.14, 2.12], [3.14, 2.12]]

    host = 'jiayiai.wicp.vip'
    client = KafkaClient(hosts="%s:29092" % host)
    print(client.topics)
    topic = client.topics['gps']

    # 创建一个kafka生产者，这是一个同步生产者
    with topic.get_sync_producer() as producer:
        while True:
            try:
                for strGps in strInfo:
                    producer.produce(str(strGps[0]) + str(strGps[1]))
            except Exception as ex:
                print('Cause Exception : %s' % (ex))
                sys.exit(0)
