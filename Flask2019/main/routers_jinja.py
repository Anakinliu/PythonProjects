from flask import Flask, render_template, request
from flask import url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
# Flask-moment依赖jQuery。js但是Bootstrap已经引入了
from datetime import datetime
# render_template()函数把jinja2m模板引擎集成到了应用中。
app = Flask(__name__)
# 扩展在创建应用实例时初始化,一种方式是将应用实例传入构造函数
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    # 参数：模板文件，键值对（表示模板变量中变量对应的具体值）
    user_agent = request.user_agent
    filter_test = '<h1>H1 HERE</h1>'  # 默认不会渲染
    # url = url_for('static',
    #               filename='css/styles.css',
    #               _external=True)
    return render_template('index_bootstrap.html',
                           agent=user_agent,
                           filter=filter_test,
                           current_time=datetime.utcnow())


@app.route('/user/<arg>')
def show_name(arg):
    return render_template('user_bootstrap.html', name=arg)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404_botstrap.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500_bootstrap.html'), 500
