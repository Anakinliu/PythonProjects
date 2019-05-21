import simpleguitk as gui


# 事件处理函数
def hi():
    print('Hi')


# 注册事件处理函数
timer = gui.create_timer(1000, hi)
# 启动计时器
timer.start()