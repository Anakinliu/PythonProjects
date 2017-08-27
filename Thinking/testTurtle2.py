import turtle
import random
import math

# square: 根据给定的边长画正方形


def square(t, length):
    for line in range(8):
        t.fd(length)
        t.lt(45)

# polygon: 绘制指定边长的正n边形


def polygon(t, length, n):
    for line in range(n):
        t.delay = 0.5
        t.fd(length + 0.0)  # 直线前进的距离
        t.lt(360 / n + 0.0)  # 转弯的角度

# 以给定的边数画圆圈,其实是36正边形,边长5, 边长x边数=圆的周长


def circle(t, r):
    round_length = r * 2 * math.pi  # 圆的周长
    n = int(r * 2 * math.pi / 3 + 1)  # 选择一个合适的边数
    polygon(t, round_length / n, n)

# 边长取一个200以内随机数

bob = turtle.Turtle()  # 初始化一个Turtle

for i in range(50):
    circle(bob, 60)

# 画完后等待用户输入

turtle.mainloop()

