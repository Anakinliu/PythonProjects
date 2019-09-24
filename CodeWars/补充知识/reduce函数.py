from functools import reduce


def sum(a, b):
    return a + b


def mul(a, b):
    return a * b


print(reduce(mul, [2, 5, 4]))