#!/usr/bin/python3
import openpyxl

wb = openpyxl.load_workbook(r'D:\workspace\jiayi\datatask\files\设备中心-设备管理.xlsx')
sh=wb[wb.sheetnames[0]]
print(sh.max_row)

for row in sh.iter_rows(min_row=4,max_row=20,min_col=10,max_col=10,values_only=True):
    for cell in row:
        print(type(cell))
        print(cell)