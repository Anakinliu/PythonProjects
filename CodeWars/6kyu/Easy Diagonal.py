import math

def c(n, m):
    # 都是可以整除的超大整数，使用整数除法：//
    return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))


def diagonal(n, p):
    return c(n, p) + c(n, p+1)
    pass

from scipy.special import comb
def diagonal(n, p):
    return comb(n+1, p+1, exact=True)

# 129100 5
print(diagonal(2155 , 51))
# print(c(66666666, 4))


