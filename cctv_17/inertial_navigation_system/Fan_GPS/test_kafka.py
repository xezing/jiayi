#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from gps_server import topic

strInfo = [[3.14, 2.12], [3.14, 2.12], [3.14, 2.12], [3.14, 2.12], [3.14, 2.12], [3.14, 2.12], [3.14, 2.12],
           [3.14, 2.12], [3.14, 2.12], [3.14, 2.12], [3.14, 2.12], [3.14, 2.12], [3.14, 2.12], [3.14, 2.12],
           [3.14, 2.12]]

if __name__ == '__main__':
    # 创建一个kafka生产者，这是一个同步生产者
    with topic.get_sync_producer() as producer:

        while True:
            try:
                for strGps in strInfo:
                    producer.produce(strGps[0] + strGps[1])
            except Exception as ex:
                print('Cause Exception : %s' % (ex))

                sys.exit(0)

