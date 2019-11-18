"""
使用正则提取url循环download
"""
import urllib.request
# 异常处理
from urllib.error import URLError, HTTPError, ContentTooShortError
import re

def download_agent_charset(url, user_agent='cqupt', num_retries = 2, charset='utf-8'):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        # 发送请求
        resp = urllib.request.urlopen(request)
        # 从请求中提取字符编码方式
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        # 解码
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

def crawl_sitemap(url):
    sitemap = download_agent_charset(url)
    # 提取sitemap链接
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    for link in links:
        download_agent_charset(link)

crawl_sitemap("http://example.python-scraping.com/sitemap.xml")
