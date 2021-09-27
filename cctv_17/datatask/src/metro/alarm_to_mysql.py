# -*- coding:utf-8 -*-

import json
import pymysql


conn = pymysql.connect(
    host='192.168.10.60',  # mysql服务器地址
    port=3306,
    user='root',  # 用户名
    passwd='jiayiAI$123',  # 密码
    db='shmetro',  # 数据库名称
    charset='utf8',  # 连接编码，根据需要填写
)
cur = conn.cursor()  # 创建并返回游标

# 根据文件内容创建表头
a = open(r"D:\workspace\jiayi\cctv_17\datatask\files\cctv17_log_0901_0907.txt", "r", encoding='UTF-8')
out = a.read()
tmp = json.dumps(out)
tmp = json.loads(out)
x = len(tmp)
print(tmp)
print(x)
# i = 0
# while i < x:
#     M = tmp[i]
#
#     E = [M['name'],M['log'],M['lat']]
#     # print(E)
#     j = len(M['children'])
#     k = 0
#     while k < j:
#         F = [M['children'][k]['name'],M['children'][k]['log'],M['children'][k]['lat'],]
#         H = E + F
#         # print(H[0])
#         sql_2 = "insert into jingweidu (prov,log,lat,city,clog,clat) values (" + "'"+H[0]+"'" +","+ "'"+H[1]+"'" + ","+"'"+H[2]+"'" + ","+"'"+H[3]+"'" + ","+"'"+H[4]+"'" + ","+"'"+H[5]+"'" + ");"
#         print(sql_2)
#         cur.execute(sql_2)  # 执行上述sql命令
#         k = k + 1
#         conn.commit()
#
#     print("============")
#     i = i+1

conn.close()
