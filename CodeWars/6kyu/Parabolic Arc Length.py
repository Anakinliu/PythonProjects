"""
我们的任务是用x在间隔[0，1]中近似表示曲线y = x * x的抛物线的长度。
我们将在点xi之间进行一个共同的步骤h：h1，h2，...，hn = h = 1 / n，并考虑曲线上的点P0，P1，P2，...，Pn。
每个Pi的坐标为（xi，yi = xi * xi）。
"""
# n : number of intervals
from math import sqrt
def len_curve(n):
    # your code
    step = 1 / n
    x0 = 0
    y0 = 0
    result = 0
    for i in range(n):
        x1 = x0 + step
        y1 = x1 * x1
        dy = y1 - y0
        result += sqrt(step * step + dy * dy)
        x0 += step
        y0 = y1
    return str(result)[:11]

def len_curve2(n):
    return round(sum(sqrt((2*k+1)**2/n/n + 1) for k in range(n))/n, 9)

# len_curve(1)# 1.414213562)
print(len_curve(10))# 1.478197397)