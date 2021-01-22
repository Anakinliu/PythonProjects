"""
输入整数半径，输出圆的面积，必须保留 7 位小数
"""
import math
n = input()


def area(r):
    r = int(r)
    print('%.7f' % (math.pi * r * r))


area(n)
