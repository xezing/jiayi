# -*- encoding: utf-8 -*-
import math
import time
import datetime
from bs4 import BeautifulSoup

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


def trans_time(t):
    t = t[:-3]
    full_time = datetime.datetime.strptime(t, "%Y%m%d%H%M%S")
    add_time = (full_time + datetime.timedelta(hours=8))
    new_time = add_time.strftime("%Y-%m-%d %H:%M:%S")
    print(new_time)

if __name__ == '__main__':
    html_doc = "<node><name>EMS</name><value>Huawei/U2000_2</value></node><node><name>ManagedElement</name><value>3145752</value></node><node><name>PTP</name><value>/rack=1/shelf=1/slot=39/domain=ptn/type=physical/port=2</value></node>"
    soup = BeautifulSoup(html_doc, "lxml")
    sibling = soup.node.next_sibling
    print(sibling.value.text)
    # print(soup.name.text)
