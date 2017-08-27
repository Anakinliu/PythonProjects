"""测试模块"""

# def 函数名 (参数，可以无参，括号必须有):
#      函数代码缩进
games = [["GTA5", [2013, [2014, 2017], 2015]], ["cs"], "ssd"]

# 递归调用
# Python默认递归调用不能超过100个，可以手动改变

# 这是一个遍历多层list的函数

"""
打印列表各项，缩进显示
"""


def get_game(some_games, level):
    for game in some_games:
        if isinstance(game, list):
            get_game(game, level+1)
        else:
            """
            builtins:
            range()

            Return an object that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
            """
            for tab in range(0, level):
                """
                builtins：
                print(self, *args, sep=' ', end='\n', file=None):

                parameter:
                end:   string appended after the last value, default a newline.
                """
                print("\t",  end='')
                if tab == level - 1:
                    print(str(game))


get_game(games, 1)

print(1, 2, 3, 4, 5, 6, 7)

"""
sep:   string inserted between values, default a space.
"""

print(1, 2, 3, 4, 5, 6, 7, sep='-')

"""model"""



