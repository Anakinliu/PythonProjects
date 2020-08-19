from datetime import datetime
"""
需要在wrapper 和 wrapper 内的调用中加入参数
"""
import functools
# 装饰器的输入输出是函数，这就是其与普通函数的不同点
def limit(g):
    @functools.wraps(g)
    def wrapper(para):
        if 9 < datetime.now().hour < 22:
            print('ok')
            g(para)
        else:
            print('not now')
    return wrapper

@limit
def game(game_title):
    print(f"gaming on {game_title}")

game("COD")
print(game.__name__)  # wrapper
# 给wrapper打上@functools.wraps(g)
print(game.__name__)  # game