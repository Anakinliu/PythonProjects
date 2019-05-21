import pandas as pd
import urllib.request as req
import json


class JDCommentsCrawler:

    def __init__(self, product_id=None, callback=None, page=1, score=0, sort_type=6):
        self.productId = product_id  # 商品ID
        self.score = score  # 评论类型（好：3、中：2、差：1、所有：0）
        self.sortType = sort_type  # 排序类型（推荐：5、时间：6）
        self.pageSize = 10
        self.callback = callback  # 回调函数，每个商品都不一样
        self.page = page  # 需要抓取的页数
        self.locationLink = 'https://sclub.jd.com/comment/productPageComments.action'
        self.paramValue = {
            'callback': self.callback,
            'productId': self.productId,
            'score': self.score,
            'sortType': self.sortType,
            'pageSize': self.pageSize,
        }
        self.locationUrl = None

    def param_dict2str(self, params):
        str1 = ''
        for p, v in params.items():
            str1 = str1 + p + '=' + str(v) + '&'
        return str1

    def concat_linkparam(self):
        self.locationUrl = self.locationLink + '?' + self.param_dict2str(self.paramValue) + 'isShadowSku=0&fold=1&page=0'
        # print(self.locationUrl)

    def request_method_page(self, p):
        # 伪装浏览器 ，打开网站
        headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
            'Referer': 'https://item.jd.com/%s.html' % (self.productId),
            'Host': 'sclub.jd.com'
        }
        url = self.locationUrl[:-1] + str(p)
        print('url : ', url)
        reqs = req.Request(url, headers=headers)
        return reqs

    def show_list_page(self, p):
        request_m = self.request_method_page(p)
        conn = req.urlopen(request_m)
        return_str = conn.read().decode('gbk')
        return_str = return_str[len(self.callback) + 1:-2]
        return json.loads(return_str)

    def save_csv(self, df, pro_id, p, score):
        # 保存文件
        df.to_csv(path_or_buf='csv/id_%s_page_%d_score_%d.csv' % (pro_id, p, score), encoding='gbk')

    def crawler(self, p):
        # 把抓取的数据存入CSV文件，设置时间间隔，以免被屏蔽
        json_info = self.show_list_page(self.page)
        tmp_list = []
        # print(json_info)
        comments = json_info['comments']
        for com in comments:
            tmp_list.append([com['content'], com['score']])
        df = pd.DataFrame(tmp_list, columns=['content', 'score'])
        self.save_csv(df, self.productId, p, self.score)
        return tmp_list


# def jdComment():
#     # 设置关键变量
#     page = 1  # 页数
#     productId = 492036  # 商品ID
#     callback = 'fetchJSON_comment98vv203899'  # 回调函数
#     JDC = JDCommentsCrawler(productId, callback, page, score=1)  # 哪种评论
#     JDC.concatLinkParam()
#     print(JDC.crawler())


# if __name__ == '__main__':
#     jdComment()
