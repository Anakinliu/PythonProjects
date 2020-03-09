"""
两个跑步的人，同一起点出发，速度相同，一个跑大权，一个小圈，不交叉，
求两人同一时间再次在起点相遇时，各跑了几圈lap

The function takes two arguments:
The length of Bob's lap (larger than 0)
The length of Charles' lap (larger than 0)

返回元组
Examples:

nbr_of_laps(5, 3) # returns (3, 5)
nbr_of_laps(4, 6) # returns (3, 2)
"""
def nbr_of_laps(x, y):
    if x == y:
        return 1, 1
    b = max(x, y)
    s = min(x, y)
    gcd = 1
    for i in range(1, s+1):
        if s % i == 0 and b % i == 0:
            if i > gcd:
                gcd = i
                pass
            pass
        pass
    print('gcd', gcd)
    if gcd == 1:
        return y, x
    else:
        lcm = x * y / gcd
        return lcm / x, lcm / y

# API大佬
from math import gcd

def nbr_of_laps2(x, y):
    lcm = x / gcd(x, y) * y
    return lcm/x, lcm/y

print(nbr_of_laps2(5, 3))