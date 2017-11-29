#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib
import threading
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
timelength = re.findall(r">\d{2,3}:\d{2}<", content)
content = []  # 去除courseID后的list
minute = []
for i in range(len(contentlist)):
    if contentlist[i] == '1b70da65-6b7f-4003-bcce-18cbbe6dea10':
        continue
    else:
        content.append((contentlist[i])[4:40])
userid = userid[0][10:46]  # 用户ID号
courseid = courseid[0][12:48]  # 课程ID号
for i in range(len(timelength)):
    if type(timelength[i][3]) == int:
        minute.append(timelength[i][1:4])
    elif type(timelength[i][3]) == str:
        minute.append(timelength[i][1:3])

# 登录的URL
loginUrl = 'http://121.250.173.149/User/DoLogin'
aboutUrl = 'http://121.250.173.149/user/GetUserInfo'
checker = 'http://121.250.173.149/User/TimingCheckUser'
saver = 'http://121.250.173.149/CourseLessonLearn/Save'
lessonsid = content
# data = {  # 不需要了, source.html内有ID, 不需要密码
#     "loginKey": "userName",
#     "username": "201512150108",
#     "password": "201512150108"
# }


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
    def __init__(self, thread_lesson_id, thread_header, thread_minute):
        threading.Thread.__init__(self)
        self.lessonid = thread_lesson_id
        self.header = thread_header
        self.minute = thread_minute

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        alive = 0
        # --------刷课线程暂时用不到, 提到了外边只运行即可--------------
        # postdata = urllib.urlencode(data)
        # # 模拟登录，并把cookie保存到变量
        # result = opener.open(loginUrl, postdata)
        # # 保存cookie到cookie.txt中
        # cookie.save(ignore_discard=True, ignore_expires=True)
        # ---------刷课线程暂时用不到, 提到了外边只运行即可-------------

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

        # times = 0
        # 一直发送 POST, 刷课代码
        while alive <= self.minute:
            # headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
            #          'Referer': 'http://121.250.173.149/Learn/Index/' + self.lessonid +
            #                    '?courseId=1b70da65-6b7f-4003-bcce-18cbbe6dea10&batchId='}

            referer = 'http://121.250.173.149/Learn/Index/' + self.lessonid + \
                      '?courseId=' + courseid + '&batchId='
            self.header['Referer'] = referer

            # CheckTimeUser可以不请求, 直接提交save
            request = urllib2.Request(checker, referer, self.header)
            # opener.open(request)
            urllib2.urlopen(request)

            # times += 1
            starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # print starttime
            # if times >= 3:
            tosaverdata = {"userId": userid,
                           "courseId": courseid,
                           "lessonId": self.lessonid,
                           "startTime": starttime,
                           "learnTime": "60",
                           "batchId": ""}  # learntime越大, 刷课跨度越快

            # 拼接url
            saverdata = urllib.urlencode(tosaverdata)
            saverrequest = urllib2.Request(saver, saverdata, self.header)
            # opener.open(request, saverdata)
            urllib2.urlopen(saverrequest)  # 此语句代替opener.open
            # times = 0
            alive += 1
            time.sleep(1)
            # print '================'
            # print alive
            # print self.minute
            # print '================'


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
# 制作请求
# postdata = urllib.urlencode(data)
# request = urllib2.Request(loginUrl, postdata, header)
# 执行正式请求
# result = urllib2.urlopen(request)  # 需要验证码了...
# print result.read()                # 需要验证码了...
# 保存cookie到cookie.txt中
# CheckTimeUser
# request = urllib2.Request(checker, postdata, headers)


# 刷课, 太快, 每节课是一个线程, 线程之间最好间隔很长

for i in range(0, 10):
    lessonid = lessonsid[i]
    # print lessonid
    print float(minute[i])
    my_thread = myThread(lessonid, header, int(minute[i]))  # str转int
    # 开启线程
    my_thread.start()
    # my_thread.join(float(minute[i]))  # 不除5了
    # if i % 5 == 0:
    #     thread.join(float(minute[i]))

print 'Main thread END'
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
