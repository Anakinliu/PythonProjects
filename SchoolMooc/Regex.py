#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

sourcefile = open('source.html')
content = sourcefile.read()
sourcefile.close()

contentlist = re.findall(r"id ?= ?\"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\"", content)
userid = re.findall(r"userId ?= ?\"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\"", content)
courseid = re.findall(r"courseId ?= ?\"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\"", content)
content = []  # 去除courseID后的list
for i in range(len(contentlist)):
    if contentlist[i] == '1b70da65-6b7f-4003-bcce-18cbbe6dea10':
        continue
    else:
        content.append((contentlist[i])[4:40])

userid = userid[0][10:46]
courseid = courseid[0][12:48]
print content
print userid
print courseid


