import requests

# r = requests.get('https://news.163.com/domestic/')
# # Response对象的重要属性
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print(r.encoding)  # 从头部的charset判断编码，默认ISO-8859-1
# print(r.apparent_encoding)  # 从内容判断编码
# r.encoding = 'GB2312'
# print(r.text)

# 不是200则抛异常
def get_html(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('发生异常')

print(get_html("https://www.cqupt.edu.cn"))