# -*- encoding: utf-8 -*-
import math
import time

"""
测试2
"""

def get_time():
    while True:
        i = input('输入数字')
        if (i == '1'):
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            return now_time
        else:
            return 0


while True:
    print(get_time())