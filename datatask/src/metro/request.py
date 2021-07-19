#!/usr/bin/python3
import requests
resp = requests.get('https://www.baidu.com')
print(resp.status_code)
print(resp.content.decode('utf8'))