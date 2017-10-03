#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd

data = xlrd.open_workbook('students.xls')

table = data.sheets()[0]

stuno_result = table.col_values(0)
stuname_result = table.col_values(1)

print type(stuno_result)

for i in range(len(stuname_result)):
    print stuname_result[i]