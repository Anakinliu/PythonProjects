import requests

url = "http://www.baidu.com/s"
w = {'wd': 'Python'}
agent = {'user-agent': 'Mozilla/5.0'}
response = requests.get(url, params=w, headers=agent)
print(response.status_code)
print(response.encoding)
response.encoding = response.apparent_encoding
print(len(response.text))
print(response.text)