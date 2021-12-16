# -*- encoding: utf-8 -*-
import os,time,random
import queue
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt = '%Y-%m-%d  %H:%M:%S %a'    #注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                    )
logging.debug("msg1")
logging.info("msg2")
logging.warning("msg3")
logging.error("msg4")
logging.critical("msg5")
"""
测试
"""

status = 0

def sub_thread_A():
    """A线程函数：生成数据"""
    while True:
        time.sleep(1)

        print(status)

def sub_thread_B():
    """B线程函数，使用数据"""
    global status
    while True:
        try:
            i = input("input=")
            status = int(i)
        except Exception as e:
            print(e)
        continue


if __name__ == '__main__':

    A = threading.Thread(target=sub_thread_A)
    A.start()
    B = threading.Thread(target=sub_thread_B)
    B.start()
