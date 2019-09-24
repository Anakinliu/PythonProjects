from urllib import request
from bs4 import BeautifulSoup
import gzip
import time

# 伪装构造头
header = {
    "Host": "www.stats.gov.cn",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/75.0.3770.142 Safari/537.36 ",
    "Referer": "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/"
}

tr_tag_name = ['citytr', 'countytr', 'towntr', 'villagetr']

base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/'
first_url = base_url + '37.html'


def get_rows(url, level):
    time.sleep(5)
    req = request.Request(url=url, headers=header)
    response = request.urlopen(req)
    # 大多数网站都对支持gzip压缩的浏览器做了gzip的压缩，在python中可以通过gzip包处理gzip压缩过的网页
    # 不能直接decode
    html = gzip.decompress(response.read())
    html = html.decode('gbk')
    # print(html)
    soup = BeautifulSoup(html, features='lxml')
    return soup.find_all("tr", {"class": tr_tag_name[level]})


rows_1 = get_rows(first_url, 0)
for r1 in rows_1:
    two_str_1 = str(r1.text)
    code_1 = two_str_1[:12]
    name_1 = two_str_1[12:]

    url_1 = str(r1.a['href'])
    #print(code_1, name_1)

    second_url = base_url + url_1
    rows_2 = get_rows(second_url, 1)
    for r2 in rows_2:
        # print(r2)
        two_str_2 = str(r2.text)
        code_2 = two_str_2[:12]
        name_2 = two_str_2[12:]
        print(name_2)
        try:
            url_2 = str(r2.a['href'])
            # print(code_2, name_2)
            third_url = base_url + "37/" + url_2
            print(third_url)
            rows_3 = get_rows(third_url, 2)
            for r3 in rows_3:
                # print('层3')
                # print(r2)
                two_str_3 = str(r3.text)
                code_3 = two_str_3[:12]
                name_3 = two_str_3[12:]

                # print(code_3, name_3)
                try:
                    url_3 = str(r2.a['href'])
                    forth_url = base_url + "37/01/" + url_3
                    rows_4 = get_rows(third_url, 3)
                    for r4 in rows_4:
                        # print('层4')
                        two_str_4 = str(r4.text)
                        code_4 = two_str_4[:12]
                        name_4 = two_str_4[12:]

                        print(code_4, name_2, name_3, name_4)
                except:
                    print(name_3 + " 3 没有下一级了")
        except:
            print(name_2 + " 2 没有下一级了")






