from flask import Flask
from flask import request
from flask import make_response  # 响应对象可以代替视图函数的元组类型返回值
from flask import redirect  # 专门用于重定向的函数
app = Flask(__name__)  # 一个应用实例
from flask import abort  # 处理错误


@app.route('/')  # 一个路由
def index():  # 一个视图函数
    user_agent = request.headers.get('User-Agent')
    response = make_response(
        '<h1>Welcome! {} browser</h1>'.format(user_agent))

    response.set_cookie('answer', '42')  # 使用响应对象进一步设置响应
    return response
    # return redirect('http://www.example.com')


@app.route('/<name>')
def show_name(name):
    # 相应代码可以作为返回的第二个参数
    # 第三个参数时HTTP响应首部字典
    return '<h2> Hello, {}!</h2>'.format(name), 404
    # return abort(404)  # 返回的页面直接显示404 NotFound


# if __name__ == '__main__':
#     app.run(debug=True)

# 有四种请求钩子，狗子与视图函数之间共享数据使用全局变量g