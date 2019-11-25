import requests

# requests.request是其他方法的基本方法
# 其他方法调用本方法
"""
**kwargs
例如params：字典或字节序列，作为参数增加到url中
例如timeout：等待服务器发送数据的时间
例如json：JSON格式的数据
headers：http头定制化，例如模拟浏览器
cookies：字典或者CookieJar，对应请求中的cookie
auth:元组，支持HTTP认证
files：字典类型，传输文件
proxies: 设定访问代理服务器
allow_redirects:重定向开关
stream：获取内容立即下载开关
verify：认证SSL证书开关
cert：本地SSL证书路径
"""
# paras
kv = {"k1": "v1",
      "k2": "v2"}
r = requests.request('GET', 'https://python123.io', params=kv)
print(r.url)

# files
fs = {'file': open('__init__.py', 'rb')}
r = requests.request('POST', 'http://python123.io/ws', files=fs)


# POST1 -字典- 被放入form中
payload = {"k": "v", 1: 2}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.status_code)
print(r.text)

# POST2 -字符串- 被放入data中
payload = "str"
r = requests.post("http://httpbin.org/post", data=payload)
print(r.status_code)
print(r.text)
