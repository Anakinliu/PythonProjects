import turtle
import math
import random


def arc(t, r, angle):
    """
    画一个圆弧
    :param t: Turtle 
    :param r: radius of the arc
    :param angle: angle of the arc
    :return: None
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1  # 边数
    step_length = arc_length / n  # 每一步的长度. 总长度/边数
    step_angle = angle / n  # 每一步画的角度, 总角度/边数

    for i in range(n):  # 画n个边
        # print(n, step_length)
        t.fd(step_length)
        t.lt(step_angle)


def petal(t, r, angle):
    """
    
    :param t: Turtle
    :param r: radius of the arc
    :param angle: angle of the arc
    :return: None
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, n, r, angle):
    """
    :param n: number of petals
    :param t: Turtle
    :param r: radius of the arc
    :param angle: angle of the arc
    :return: 
    """

    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)

t = turtle.Turtle()
for i in range(1500):  # 阿基米德螺旋线
    print(i)
    arc(t, i, 6)
# t.speed(1000)
# flower(t, 20, 300, 30)

# def flower(t, r, angle, n):
#     real_n = 2 * n  # 真正要画的边数
#     reverse = 0
#     for i in range(real_n):
#         if reverse == 0:
#             reverse = 1
#             arc(t, r, angle)
#         else:
#             reverse = 0





