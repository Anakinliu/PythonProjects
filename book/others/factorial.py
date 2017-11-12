"""
计算n的阶乘
"""


def factorial(n):
    if n < 0:
        return None
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


result = factorial(44)
print(result)
