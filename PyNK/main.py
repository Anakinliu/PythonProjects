from requests import Request, Session
from requests import Response
from datetime import datetime
import time

def post_form():
    print('post form start...')
    request_url = 'http://222.180.221.78:9090/web/connect'

    request_headers = {
        'Accept': '* / *',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh',

        'Cache - Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '241',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': '222.180.221.78:9090',
        'Origin': 'http://222.180.221.78:9090',
        'Pragma': 'no-cache',
        'Referer': 'http:/222.180.221.78:9090/web',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.88 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    payload = {
        'web-auth-user': '15310258947@cqupt',
        'web-auth-password': '19970823',
        'remember-credentials': 'on',
        'redirect-url': 'http://127.0.0.1:9091/?source-ip=172.33.0.92&wlanacname=183.64.60.82&nas-ip=183.64.60.82'
                        '&source-mac=e0-94-67-71-ff-b1 '
    }

    session = Session()

    requset_cookies = {
        'redirect-url': 'http://127.0.0.1:9091/?source-ip=172.33.0.92&wlanacname=183.64.60.82&nas-ip=183.64.60.82&source-mac=e0-94-67-71-ff-b1',
        'remember': 'true',
        'session-context': 'eyJzY29wZSI6IlBPUlRBTF9DT05URVhUX1RPS0VOX1NDT1BFIiwicmFuZG9tIjoiNW83ajVkTzB6Vmh3UERmOE4yZVRZUjNuM3VMd0t5UDQiLCJkaWdlc3QiOiI4ZWY1NDk4NmRlNDg4YzAzZGRhNmU4Y2RjZDU3MTUyOTU4YjlkNmNmMDY4ZmUzMzM0ZWI2MTZhMGMyMjkxNjc5IiwiY3JlYXRpb25fdGltZSI6MTU3ODQ2NTE5NjQzNiwiZXh0ZW5kZWRfaW5mb3JtYXRpb24iOiJ7XCJpcFwiOlwiMTcyLjMzLjAuOTJcIixcIm1hY1wiOlwiZTA6OTQ6Njc6NzE6ZmY6YjFcIixcIm5hc19pcFwiOlwiMTgzLjY0LjYwLjgyXCIsXCJzZXNzaW9uXCI6XCIyMzg5Mzc1XCJ9In0=',
        'username': '15310258947@cqupt'
    }

    req = Request('POST', request_url,
                  data=payload,
                  headers=request_headers,
                  )
    prepped = session.prepare_request(req)
    resp = session.send(prepped)

    # while resp.status_code != 200:
    #     prepped.prepare_cookies(cookies)
    #     resp = session.send(prepped)
    #     print(resp.status_code)
    #     time.sleep(2)

    print(resp.status_code)


post_form()
