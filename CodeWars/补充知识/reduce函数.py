from functools import reduce

from itertools import groupby

def sum(a, b):
    return a + b


def mul(a, b):
    return a * b

def fuck(v, _):
    print('v is: ', v)
    v.append(0)
    return v
lst = range(2)
# reduce函数参数： 函数名， 序列[，初始化序列]
print(reduce(sum, lst))
# 计算阶乘。。。
print(reduce(mul, range(1, 4)))
lst2 = [1, 3, 5, -1, 10, 0, 999, 100, -9, -12, -3, 1]
# 求最大值。。。
print(reduce(lambda a, b : a if a > b else b, lst2))
# print(reduce(fuck,lst, [1,2,3]))
#BEGIN 相当于
# it = iter(lst)  # 生成迭代器，参数是支持迭代的对象
# value = [1,2,3]
# for i in it:
#     value = fuck(value, i)
# print(value)
#END#
"""
第一步，选择序列的前两个元素并获得结果。
下一步是对先前获得的结果应用相同的功能，并且紧随第二个元素之后的数字将被再次存储。
继续此过程，直到容器中没有剩余元素为止。
返回的最终结果将返回并打印在控制台上。
"""



