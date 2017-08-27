import random

"""计算机随机模拟方法,也叫蒙特卡罗方法,即使用伪随机数解决一些问题"""

# 在边长为2的正方形内做一个最大内接圆,测试: 在正方形内随机选取一点,落在圆内的概率.

"""TODO: 使用其他更精确的方法得到pai!!"""
n = 1000000

k = 0

t = 10
for f in range(t):
    k = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        # 如果在圆内
        if x ** 2 + y ** 2 < 1:
            k += 1
    print(4 * float(k) / float(n))