from flask import Flask, render_template, request, url_for, jsonify
from flask_bootstrap import Bootstrap
from crawler import JDCommentsCrawler
import urllib
from csv_handler import CSVHandler

app = Flask(__name__)
# 扩展在创建应用实例时初始化,一种方式是将应用实例传入构造函数
bootstrap = Bootstrap(app)

# 商品ID与回调函数
# 按销量选了三个牌子的，1 小米 2 公牛 3 良品 4 飞利浦
param_list = [['4354506', 'fetchJSON_comment98vv3810'],
                ['492036', 'fetchJSON_comment98vv203899'],
                ['5342704', 'fetchJSON_comment98vv774'],
              ['4130061', 'fetchJSON_comment98vv4666'],
              ]

# init
csv_handler = CSVHandler()


@app.route('/')
def index():
    return render_template('index_bootstrap.html')


@app.route('/crawler')
def crawler():
    return render_template('crawler_bootstrap.html')


@app.route('/_get_reviews')
def get_reviews():
    # 参数名， 默认值，需要转换的类型
    # page = request.args.get('page', type=int)
    # print("得到的page为", page)
    start_page = request.args.get('start_p', type=int)
    end_page = request.args.get('end_p', type=int)
    brand = request.args.get('brand', type=int)  # 1 小米
    score = request.args.get('score', type=int)
    print(str(start_page), ' ', str(end_page), ' ', str(brand), ' ', str(score))
    # b = request.args.get('b', 0, type=int)
    # 设置关键变量
    # page = 1  # 页数
    # product_id = 492036  # 商品ID
    # callback = 'fetchJSON_comment98vv203899'  # 回调函数
    # score = 0  # 0所有 ，1-3 差-好
    jd_crawler = JDCommentsCrawler(param_list[brand][0],
                                   param_list[brand][1],
                                   start_page,
                                   score=3-score)
    jd_crawler.concat_linkparam()
    try:
        res = jd_crawler.crawler(start_page)
    except urllib.error.URLError as e:
        print(e)
        res = [[]]
    # print(JDC.crawler())
    return jsonify(result=res)


@app.route('/all_csv')
def all_csv():
    return render_template('csv_bootstrap.html')


@app.route('/_get_first_csv')
def get_first_csv():
    cla = request.args.get('cla', 0, type=int)
    count, res = csv_handler.get_first(cla)
    return jsonify(count=count, result=res)


@app.route('/_get_want_csv')
def get_want_csv():
    want_index = request.args.get('want_index', 1, type=int)
    res = csv_handler.get_want(want_index)
    print(res)
    return jsonify(result=res)


@app.route('/do_data')
def do_data():
    return render_template('data_bootstrap.html')


@app.route('/learn_data')
def learn_data():
    return render_template('learn_bootstrap.html')

# @app.route('/_get_saved_reviews')
# def get_saved_reviews():
#
#
# if __name__ == '__main__':
#     app.run()
