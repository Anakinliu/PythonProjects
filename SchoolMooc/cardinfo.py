#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib
import threading
import json
import time
import re
import xlrd

# 查询的URL
infourl = 'http://www.ejf365.com/ESCHOOLWEB/neweschool/front/getCardInfo'

f = open("out.txt", "w")

# 读取xls文件获取学号与姓名
data = xlrd.open_workbook('students.xls')
table = data.sheets()[0]
stuno_result = table.col_values(0)
stuname_result = table.col_values(1)

# 'stuName=%E5%88%98%E5%8D%B0%E5%85%A8 ' \
# 'stuNo=201512180119' \
# 'shanghuMode=1' \
# 'schoolId=20170420090738477000057900' \
# 'childSchoolId=' \
# 'cardApiId=20170609092157205000006685' \
# 'payMachine=p' \
# 'onecard_stuno_tip=%E7%BC%96%E5%8F%B7' \
# 'onecard_stuno_map=0' \
# 'schoolType='

data = {
    "stuName": "全文浩",
    "stuNo": "201301110124",
    "shanghuMode": "1",
    "schoolId": "20170420090738477000057900",
    "childSchoolId": "",
    "cardApiId": "20170609092157205000006685",
    "payMachine": "p",
    "onecard_stuno_tip": "%E7%BC%96%E5%8F%B7",
    "schoolType": ""
}

connection = 'keep-alive'
accept = 'application/json, text/plain, */*'
origin = 'http://www.ejf365.com'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit' \
             '/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Saf' \
             'ari/537.36'
# 设置content-type会导致500?
# content_type = 'application/json;charset=UTF-8'
referer = 'http://www.ejf365.com/ESCHOOLWEB/neweschool/front/cardquery?orgid='
accept_encoding = 'gzip, deflate'
accept_language = 'zh-CN,zh;q=0.8'
header = {'Connection': connection,
           'Accept': accept,
           'Origin': origin,
           'User-agent': user_agent,
           'Referer': referer,
           'Accept-Encoding': accept_encoding,
           'Accept-Language': accept_language}

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
    def __init__(self, stuno, stuname):
        threading.Thread.__init__(self)
        self.data = {
            "stuName": stuname.encode("UTF-8"),
            "stuNo": stuno.encode("UTF-8"),
            "shanghuMode": "1",
            "schoolId": "20170420090738477000057900",
            "childSchoolId": "",
            "cardApiId": "20170609092157205000006685",
            "payMachine": "p",
            "onecard_stuno_tip": "%E7%BC%96%E5%8F%B7",
            "schoolType": ""
        }
        # self.stuno = stuno
        # self.stuname = stuname

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        # self.data['stuNo'] = self.stuno
        # self.data['stuName'] = self.stuname
        # print self.data
        # 制作请求
        postdata = urllib.urlencode(self.data)
        request = urllib2.Request(infourl, postdata, header)
        # 执行正式请求
        result = urllib2.urlopen(request)
        result_dict = eval(result.read())
        # print result_dict
        # print type(result_dict)
        if result_dict['state'] != '0':
            print >> f, "%s || %s || %s" % (result_dict['stuName'], result_dict['stuNo'], result_dict['balance'])
            # print result_dict['stuName'] + ' || ' + result_dict['stuNo'] + ' || ' + result_dict['balance']
        else:
            print self.data['stuName'] + ' || ' + self.data['stuNo'] + ' || ' + '无法查询!'



# 模拟登录，并把cookie保存到变量, 不用cookie也能刷课...
# result = opener.open(loginUrl, postdata)
# 保存cookie到本地
# cookie.save(ignore_discard=True, ignore_expires=True)
# ---------------------------
# 制作请求
# postdata = urllib.urlencode(data)
# request = urllib2.Request(infourl, postdata, header)
# # 执行正式请求
# result = urllib2.urlopen(request)
# result_dict = eval(result.read())
# print result_dict
# print type(result_dict)
# if result_dict['state'] != '0':
#     print result_dict['stuName'] + ' || ' + result_dict['stuNo'] + ' || ' + result_dict['balance']
# else:
#     print data['stuName'] + ' || ' + data['stuNo'] + ' || ' + '无法查询!'
# ---------------------------------
# 保存cookie到cookie.txt中
# CheckTimeUser
# request = urllib2.Request(checker, postdata, headers)

# {'stuName': '\xe5\x85\xa8\xe6\x96\x87\xe6\xb5\xa9',
#  'stuNo': '201301110124',
#  'schoolId': '20170420090738477000057900',
#  'cardApiId': '20170609092157205000006685',
#  'schoolType': '',
#  'payMachine': 'p',
#  'childSchoolId': '',
#  'onecard_stuno_tip': '%E7%BC%96%E5%8F%B7',
#  'shanghuMode': '1'}

# 刷课, 太快, 每节课是一个线程, 线程之间最好间隔很长, 否则首页显示动态!

for i in range(1, 13000):
    thread = myThread(stuno_result[i], stuname_result[i])  # str转int
    # 开启线程
    thread.start()
    if i % 100 == 0:
        thread.join()

print 'Main END'
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
