#!/usr/bin/python
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

# 获取ID, 包含重复的?
sourcefile = open('source.html')
content = sourcefile.read()
sourcefile.close()
contentlist = re.findall(r"id=\"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\"", content)
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

# 登录的URL
loginUrl = 'http://121.250.173.149/User/DoLogin'
aboutUrl = 'http://121.250.173.149/user/GetUserInfo'
checker = 'http://121.250.173.149/User/TimingCheckUser'
saver = 'http://121.250.173.149/CourseLessonLearn/Save'
lessonsid = content
data = {
    "loginKey": "userName",
    "username": "201512180119",
    "password": "....."
}


def hh(username, password):
    dataarg = {"loginKey": "userName", "username": username, "password": "123456", 'password': password}
    for i in range(10):
        if i < 10:
            dataarg['username'] = '20151218010' + str(i)
        else:
            dataarg['username'] = '2015121801' + str(i)
        print dataarg
        postdata = urllib.urlencode(dataarg)
        # 模拟登录，并把cookie保存到变量
        result = opener.open(loginUrl, postdata)
        # 保存cookie到cookie.txt中
        cookie.save(ignore_discard=True, ignore_expires=True)
        sure = result.read()
        print sure


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, username, password, lessonid):
        threading.Thread.__init__(self)
        self.data = {"loginKey": "userName", "username": username,
                     "password": password}
        self.lessonid = lessonid

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数

        postdata = urllib.urlencode(self.data)
        # 模拟登录，并把cookie保存到变量
        result = opener.open(loginUrl, postdata)
        # 保存cookie到cookie.txt中
        cookie.save(ignore_discard=True, ignore_expires=True)
        # ---------------START-------------
        # sure = json.loads(result.read())
        # if sure[u'errorCode'] == 1:  # 成功登录
        #     print self.data['username'] + r'\\//' + self.data['password']
        #     about1 = opener.open(aboutUrl)
        #     about2 = json.loads(about1.read())
        #     print '=================================='
        #     userid = about2[u'UserInfo'][u'Id']
        #     if about2[u'User'][u'fullName'] is not None:
        #         print about2[u'User'][u'fullName']
        #         if about2[u'UserInfo'][u'user_mobile'] is not None:
        #             print about2[u'UserInfo'][u'user_mobile']
        #         else:
        #             print about2[u'User'][u'fullName'] + "'s mobile is None."
        #         if about2[u'User'][u'about'] is not None:
        #             print about2[u'User'][u'about']
        #         else:
        #             print about2[u'User'][u'fullName'] + "'s about is None."
        #     else:
        #         print self.data['username'] + ' no fullname!'
        #         if about2[u'UserInfo'][u'user_mobile'] is not None:
        #             print about2[u'UserInfo'][u'user_mobile']
        #         else:
        #             print self.data['username'] + "'s mobile is None."
        #         if about2[u'User'][u'about'] is not None:
        #             print about2[u'User'][u'about']
        #         else:
        #             print self.data['username'] + "'s about is None."
        #     print '=================================='
        # print about2[u'User'][u'about']
        # ---------------END-------------

        times = 0
        # 一直发送 POST
        while True:
            headers = 'http://121.250.173.149/Learn/Index/' + self.lessonid +\
                      '?courseId=1b70da65-6b7f-4003-bcce-18cbbe6dea10&batchId='
            request = urllib2.Request(checker, headers)
            opener.open(request)
            times += 1
            starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # print starttime
            if times >= 3:
                    request = urllib2.Request(saver, headers)
                    tosaverdata = {"userId":userid,
                                   "courseId":courseid,
                                   "lessonId":self.lessonid,
                                   "startTime":starttime,
                                   "learnTime":"3600",
                                   "batchId":""}  # learntime越大, 刷课跨度越快
                    # 拼接url
                    saverdata = urllib.urlencode(tosaverdata)
                    opener.open(request, saverdata)
                    times = 0


# 刷课, 太快, 每节课是一个线程, 线程之间最好间隔很长, 否则首页显示动态!
for i in range(0, len(content)):
    lessonid = lessonsid[i - 1]
    # print lessonid
    thread = myThread(data['username'], data['password'], lessonid)
    # 开启线程
    thread.start()


# 创建新线程
# for i in range(19, 20):
#     if i < 10:
#         data['username'] = '20151218010' + str(i)
#     else:
#         data['username'] = '2015121801' + str(i)
#     thread = myThread(data['username'], data['password'])
#     # 开启线程
#     thread.start()

# pool = threadpool.ThreadPool(10)  # 建立线程池，控制线程数量为10
#
# #  构建请求，get_title为要运行的函数，data为要多线程执行函数的参数，最后这个print_result是可选的，是对前两个函数运行结果的操作
# reqs = threadpool.makeRequests(myThread(data['username'], data['username']))
# pool.wait()  #线程挂起，直到结束

