import requests

try:
    response = requests.get("https://item.jd.com/2967929.html")
    print(response.status_code)
    print(response.encoding)
    print(response.text)
except:
    print('fail')