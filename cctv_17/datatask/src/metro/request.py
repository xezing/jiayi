#!/usr/bin/python3
import requests
resp = requests.get('http://10.17.200.88/logger/v1/user-log/search?f_gt_createTimeStr=2021-07-05%2011:22:55&f_lt_createTimeStr=2021-07-06%2011:22:55&f_sort_createTimeStr=desc&randomABC=922141334995&page_num=1&page_size=15')
print(resp.status_code)
resp.json()
print(resp.content.decode('utf8'))