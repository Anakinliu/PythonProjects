import requests
import os

url = 'http://222.180.221.78:9090/images/bg2.png'
root = 'x://'
file_name = url.split('/')[-1]
path = root + file_name
# print(path)
try:
    response = requests.get(url)
    print(response.status_code)
    # print(response.content)
    with open(path, 'wb+') as f:
        # 注意对非文字类一般以字节方式读取
        f.write(response.content)
except:
    print('fail')