# 就是一个小说

import requests
from lxml import etree
def get_list(url):
    html = requests.get(url).content
    # print(html)
    tree = etree.HTML(html)
    contents = tree.xpath('//*[@id="list"]/dl')
    # print(len(contents))
    # print(contents)
    links = []
    links = contents[0].xpath('dd/a/@href')
    for link in links:
        # print(link)
        c_html = requests.get('http://www.yuetut.com' + link).text
        c_tree = etree.HTML(c_html)
        # title = c_tree.xpath('//*[@id="wrapper"]/div[3]/div/div[2]/h1/text()')
        content = c_tree.xpath('//*[@id="content"]/text()')
        # print(title, content)
        print(content)

    return html

get_list('http://www.yuetut.com/cbook_17688/')
