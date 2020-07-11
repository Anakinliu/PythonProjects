"""
https://www.codewars.com/kata/599688d0e2800dda4e0001b0

0,1,2,3,4,5,6,7,8,9,10,22,11,20,13,24.。。。
所有数只出现一次
0-10忽略，22不会包含1和0的最小数，11是不包含2的最小数
"""


def judge(n, base, lst):
    if base in lst:
        return True
    num_str = str(n)
    base_str = str(base)
    has = False
    for d in num_str:
        if base_str.count(d):
            has = True
            break
    return has


def find_num(n):
    """
    :param n: 索引
    :return: 返回索引对应的元素
    """
    lst = [i for i in range(11)]
    if n <= 10:
        return lst[n]
    idx = 10
    while idx < n:
        base = 11
        # 循环，找到下一个数
        while judge(lst[idx], base, lst):
            print(base)
            base += 1
            if base in lst:
                continue
        print('----')
        # 添加这个数
        lst.append(base)
        idx += 1
    print(lst)
    return lst[n]

# print(find_num(15))

# x = '123'
# for i in reversed(x):
#     print(i)
# print(x)  # 不变

# x = [11,22]
# print(22 in x)


"""
daddepledge
利用了集合的解法，简短
"""
M = [0]

while len(M) <= 500:
    k, s = 0, {c for c in str(M[-1])}
    while k in M or bool({c for c in str(k)} & s):  # 两个集合没有一个元素相同时，集合进行或操作结果是空，if视为False
        k += 1
    M.append(k)

find_num_clever = lambda n: M[n]

# print(find_num_clever(15))

a = set('ab')
b = set('cda')
s = 'qwer'
c = {i for i in s}
print(type(c))
if bool(a & b):
    print('ok')

