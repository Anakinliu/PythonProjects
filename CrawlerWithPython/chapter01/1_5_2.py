import urllib.request
# 异常处理
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url, num_retries = 2):
    print('Downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error: ', e.reason)
        html = None
        if num_retries > 0:
            # 只在遇到5xx错误代码时重试
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # revursively retry 5xx HTTP errors
                return download(url, num_retries-1)
        else:
            print('three times retries failed , exit.')
    return html

download('http://meetup.com')
