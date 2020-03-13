import math

def jc(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result


def c(n, m):
    # return int(math.factorial(n)) / int((math.factorial(m)) * int(math.factorial(n - m)))
    return jc(n) / (jc(m) * jc(n - m))


def diagonal(n, p):
    return int(c(n, p) + c(n, p+1))




    pass

# 129100 5
print(diagonal(3591, 153))
# print(c(66666666, 4))


