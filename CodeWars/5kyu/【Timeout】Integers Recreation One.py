"""
42 的因子为 : 1, 2, 3, 6, 7, 14, 21, 42.
因子的平方为 : 1, 4, 9, 36, 49, 196, 441, 1764.
因子平方的和为 ： 2500 is 50 * 50, a square!
给定两个整数m，n（1 <= m <= n），我们想找到m和n之间的所有整数，它们的平方除数之和本身就是一个平方。
42就是这样一个数字。

Examples:
list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
"""
import math


def list_squared(m, n):
    # your code
    res = []
    for e in range(m, n+1):
        # s = 1
        s = set()
        for d in range(1, int(math.sqrt(e) + 1)):
            if e % d == 0:
                s.add(d**2)
                s.add((e // d) ** 2)
                pass
            pass
        s.add(e ** 2)
        # print(s)
        # sq = math.floor(math.sqrt(s))  # 计算这些和的平方根的下整数
        # if s == sq ** 2:
        #     res.append([e, s])
        # 是否是整数
        ss = sum(s)
        if math.sqrt(ss) % 1 == 0:
            res.append([e, ss])
        pass
    # print(res)
    return res

list_squared(1, 100)
