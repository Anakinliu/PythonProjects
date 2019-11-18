"""
使用url规律下载,利用itertools
"""
import itertools
import urllib.request
# 异常处理
from urllib.error import URLError, HTTPError, ContentTooShortError

def download_agent(url, user_agent='wswp', num_retries = 2, charset='utf-8'):
    print('Downloading:', url)
    # 构造请求
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
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

def crawl_site(url):
    for page in itertools.count(1):
        pg_url = f'{url}{page}'
        html = download_agent(pg_url)
        if html is None:
            break

crawl_site('http://exapmle.python-scraping.com/view/')
