"""
返回比给定数值更大一点的数，没有则返回 -1

12 ==> 21
513 ==> 531
2017 ==> 2071
"""

"""
 commit: 4KYU 是一个新世界啊！！！
"""
import itertools

def permutationsD(arr, position, end, res=[]):
    if position == end:
        res.append(int(''.join(arr)))

    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end, res)
            arr[index], arr[position] = arr[position], arr[index]


def next_bigger2(n):
    n_str = str(n)
    lst = list(n_str)
    len_ = len(lst)
    bigger = -1
    for i in range(1, len_):
        use_str = list(n_str[-1-i:])
        res = []
        permutations(use_str, 0, len(use_str), res)
        res.sort()
        for j in res:
            if j > n:
                bigger = j
                break
        if bigger != -1:
            break
    print(bigger)
    return bigger


# next_bigger2(122)
#
# arr = ["1","2","2"]
# res = []
# permutations(arr, 0, len(arr), res)
# print(res)




def next_bigger3(n):
    n_str = str(n)
    lst = list(n_str)
    len_ = len(lst)
    res = list(itertools.permutations(lst, len_))
    res.sort()
    bigger = -1
    for i in res:
        num = int(''.join(list(i)))
        if num > n:
            bigger = num
            break
    print(bigger)
    return bigger
#
#


def per(lst):
    res = list(itertools.permutations(lst, len(lst)))
    res.sort()
    return res

def next_bigger4(n):
    n_str = str(n)
    lst = list(n_str)
    len_ = len(lst)
    bigger = -1
    for i in range(len_):
        s = n_str[-2-i:]
        per_lst = per(s)
        for j in per_lst:
            new = n_str[:-2-i] + j
            if int(new) > n:
                bigger = new
                break
        if bigger != -1:
            break

    print(bigger)
    return bigger


# next_bigger4(12354674987)

def p(n):
    digits = []
    b = n % 10
    a = n // 10
    digits.append(b)
    while a:
        b = a % 10
        a = a // 10
        digits.append(b)
    res = []
    z = 1
    print(res)

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))  # index的复数形式
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])  # 第一次返回原iterable
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


for j in permutations('123'):
    print(j)
