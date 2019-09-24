# 我的解


def split_digit(n):
    digit_lst = []
    while n > 0:
        m = n % 10
        n = n // 10
        digit_lst.append(m)
    return digit_lst


def multi_res(lst):
    result = 1
    for i in lst:
        result = result * i
    return result


def persistence(n):
    # your code
    digit_lst = split_digit(n)
    count = 0
    while len(digit_lst) > 1:
        count = count + 1
        multi = multi_res(digit_lst)
        # print("multi = ", multi, "digittal = ", digit_lst)
        digit_lst = split_digit(multi)
    # print(digit_lst)
    return count


# print(persistence(4))

# 大神解
import operator
from functools import reduce


def persistence_2(n):
    i = 0
    while n >= 10:
        # 1. 使用字符串分割数字每个位
        # 2. 使用reduce函数逐个相乘
        n = reduce(operator.mul, [int(x) for x in str(n)])
        print(n)
        i += 1
    return i


# print('result ', persistence_2(999), str())


# 实现reduce函数
def my_reduce(func, seq, initial=None):
    if len(seq) < 1:
        return 0
    res = seq[0]
    if initial is not None:
        res = func(res, initial)
    for e in seq[1:]:
        res = func(res, e)
    return res


def bug(x, y):
    return 7
# print(my_reduce(lambda x, y: x * y, [1, 2, 3], 11))
print(reduce(bug, [1, 2, 3]))
print(my_reduce(bug, [1, 2, 3]))




