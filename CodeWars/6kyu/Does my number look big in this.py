import operator
from functools import reduce

# 我的解
def narcissistic(value):
    str_value = str(value)
    power = len(str_value)
    digits = [int(x) ** power for x in str_value]
    print(digits)
    multi = reduce(operator.add, digits, 0)
    return multi == value


print(narcissistic(372))

# 大神解
def narcissistic_2(value):
    return value == sum(int(e) ** len(str(value)) for e in str(value))


print(narcissistic_2(371))
