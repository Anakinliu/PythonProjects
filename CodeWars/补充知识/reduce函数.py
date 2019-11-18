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
print(reduce(fuck,lst, [1,2,3]))
#BEGIN 相当于
it = iter(lst)  # 生成迭代器，参数是支持迭代的对象
value = [1,2,3]
for i in it:
    value = fuck(value, i)
print(value)
#END#



