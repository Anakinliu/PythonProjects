#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

sourcefile = open('source.html')
content = sourcefile.read()
sourcefile.close()

contentlist = re.findall(r"id ?= ?\"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\"", content)
userid = re.findall(r"userId ?= ?\"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\"", content)
courseid = re.findall(r"courseId ?= ?\"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\"", content)
timelength = re.findall(r">\d{2,3}:\d{2}<", content)
content = []  # 去除courseID后的list
minute = []
for i in range(len(contentlist)):
    if contentlist[i] == '1b70da65-6b7f-4003-bcce-18cbbe6dea10':
        continue
    else:
        content.append((contentlist[i])[4:40])

userid = userid[0][10:46]
courseid = courseid[0][12:48]

print len(content)
print userid
print courseid
print type(timelength[0][3])
for i in range(len(timelength)):
    if type(timelength[i][3]) == int:
        minute.append(timelength[i][1:4])
    elif type(timelength[i][3]) == str:
        minute.append(timelength[i][1:3])

print minute
print int(minute[2]) == 8

## 找出相邻5节课中最长的

