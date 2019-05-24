from flask import Flask, render_template, request, Response, url_for, jsonify
from flask_bootstrap import Bootstrap

import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import os
# 项目内
from crawler import JDCommentsCrawler
from csv_handler import CSVHandler
from participle import Participle
from word_2_vec import W2V
from plot import create_figure
from threading import Thread
import tensorflow as tf


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
part = None
w2v = W2V()
his = {}

# 。。。
graph = tf.get_default_graph()


@app.route('/')
def index():
    return render_template('index_bootstrap.html')


@app.route('/crawler')
def crawler():
    return render_template('crawler_bootstrap.html')


@app.route('/_get_reviews')
def get_reviews():
    if os.path.exists(Participle.path + ".npy"):
        os.remove(Participle.path + ".npy")
    if os.path.exists("csv/np/score.py.npy"):
        os.remove("csv/np/score.py.npy")
    # 参数名， 默认值，需要转换的类型
    # page = request.args.get('page', type=int)
    # print("得到的page为", page)
    start_page = request.args.get('start_p', 1, type=int)
    end_page = request.args.get('end_p', 1, type=int)
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
        print('打印', e)
        res = [[]]
    print('res', res)
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


@app.route('/participle')
def participle():
    return render_template('participle_bootstrap.html')


@app.route('/learn_data')
def learn_data():
    return render_template('train_bootstrap.html')


@app.route('/_do_participle')
def _do_participle():
    global part
    # 弄个线程也没看出来有啥用
    part = Participle(csv_handler)
    if os.path.exists(Participle.path + ".npy") is False:
        part.start()
        part.join()  # 阻塞主线程
    return jsonify(result=1)  # 返回1代表分词保存完了


@app.route('/_get_participle')
def _get_participle():
    # 这里就没用线程
    start_index = request.args.get('start_index', 1, type=int)
    print('start index: ', start_index)
    res = part.get_want_participle(start_index)
    fin = []
    for i in res:
        fin.append(' | '.join(i))
    return jsonify(r=fin, c=part.get_num())


@app.route('/word_2_vec')
def word_2_vec():
    return render_template('word2vec_bootstrap.html')


@app.route('/_do_convert')
def _do_convert():
    w2v.convert()
    return jsonify(result=1)


@app.route('/_get_sim')
def _get_sim():
    input_word = request.args.get('input_word', type=str)
    print(input_word, type(input_word))
    res = w2v.sim(input_word)
    return jsonify(result=res)


import train_model
dl = train_model.DL()


@app.route('/_do_fit')
def _do_fit():
    ep = request.args.get('epochs', 5, type=int)
    if ep < 5:
        ep = 5
    global graph
    with graph.as_default():
        global dl
        dl = train_model.DL()
        dl.set_epochs(ep)
        # print(ep, '-------------------------------------')
        dl.run()
    return jsonify(res=1)


@app.route('/plot_1.png')
def _do_plot_1():
    # input_word = request.args.get('input_word', type=str)
    global dl
    fig = dl.show(0)
    # fig = w2v.get_fig()

    # fig = create_figure()  # from plot import create_figure
    output = io.BytesIO()
    f1 = FT(output, fig)
    f1.start()
    f1.join()
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/plot_2.png')
def _do_plot_2():
    global dl
    fig = dl.show(1)
    # fig = w2v.get_fig()

    # fig = create_figure()  # from plot import create_figure
    output = io.BytesIO()
    f2 = FT(output, fig)
    f2.start()
    f2.join()
    return Response(output.getvalue(), mimetype='image/png')


# 耗时IO
class FT(Thread):

    def __init__(self, output, fig):
        super().__init__()
        self.output = output
        self.fig = fig

    def run(self):
        FigureCanvas(self.fig).print_png(self.output)


@app.route('/use_model')
def use_model():
    return render_template('use_bootstrap.html')


@app.route('/_get_pre')
def _get_pre():
    input_review = request.args.get('input_review', type=str)
    import use_model
    global graph
    with graph.as_default():
        print('获得的用户输入', input_review)
        res, probs = use_model.predict(input_review)
        print('模型结果', res)
    return jsonify(res=res, probs=probs)


@app.route('/test.png')
def plot_png():
    fig = w2v.get_fig()

    # fig = create_figure()  # from plot import create_figure
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

# @app.route('/_get_saved_reviews')
# def get_saved_reviews():
#
#
# if __name__ == '__main__':
#     app.run()
