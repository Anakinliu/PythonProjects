#!/usr/bin/python
# -*- coding: UTF-8 -*-


#!/usr/bin/python_snake
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib
import threading
import json
import time
import re

filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

data = {
    "loginKey": "userName",
    "username": "onlyyou",
    "password": "123456......"
}

# 登录的URL
loginUrl = 'http://121.250.173.149/User/DoLogin'
aboutUrl = 'http://121.250.173.149/user/GetUserInfo'
checker = 'http://121.250.173.149/User/TimingCheckUser'
saver = 'http://121.250.173.149/CourseLessonLearn/Save'
process = 'http://121.250.173.149/User/ProcessRequest2'

connection = 'keep-alive'
accept = 'application/json, text/plain, */*'
origin = 'http://121.250.173.149'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit' \
             '/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Saf' \
             'ari/537.36'
# 设置content-type会导致500?
# content_type = 'application/json;charset=UTF-8'
referer = 'http://121.250.173.149/Home/HomePage'
accept_encoding = 'gzip, deflate'
accept_language = 'zh-CN,zh;q=0.8'
header = {'Connection': connection,
           'Accept': accept,
           'Origin': origin,
           'User-agent': user_agent,
           'Referer': referer,
           'Accept-Encoding': accept_encoding,
           'Accept-Language': accept_language}
# 模拟登录，并把cookie保存到变量, 不用cookie也能刷课...
# result = opener.open(loginUrl, postdata)
# 保存cookie到本地
# cookie.save(ignore_discard=True, ignore_expires=True)

request = urllib2.Request(loginUrl, header)
result = urllib2.urlopen(process)
print result.read()


# 制作请求
# postdata = urllib.urlencode(data)                --------------
# request = urllib2.Request(loginUrl, postdata, header)         ---------------

# 执行正式请求
# result = urllib2.urlopen(request)  # 需要验证码了...
# print result.read()                # 需要验证码了...
# 保存cookie到cookie.txt中
# CheckTimeUser
# request = urllib2.Request(checker, postdata, headers)


# 刷课, 太快, 每节课是一个线程, 线程之间最好间隔很长, 否则首页显示动态!

# for i in range(1, len(lessonsid)):
#     lessonid = lessonsid[i]
#     # print lessonid
#     print minute[i]
#     thread = myThread(lessonid, header, int(minute[i]))  # str转int
#     # 开启线程
#     thread.start()
#     if i % 5 == 0:
#         thread.join()

print 'Main END'

