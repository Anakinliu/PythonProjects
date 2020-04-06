"""
https://www.codewars.com/kata/555624b601231dc7a400017a/
"""

"""
假设将n个人围成一个圈，并按照每k个步骤将其淘汰，直到剩余最后一个生还者，
josephus_survivor(7,3) => means 7 people in a circle;
one every 3 is eliminated until one remains
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out
[1,2,4,5,7] => 6 is counted out
[1,4,5,7] => 2 is counted out
[1,4,5] => 7 is counted out
[1,4] => 5 is counted out
[4] => 1 counted out, 4 is the last element - the survivor!
"""
# 会超时！！！
def josephus_survivor_a(n,k):
    #your code here
    lst = list(range(1, n+1))
    c = 0
    i = 0
    while len(lst) > 1:
        c += 1
        if c == k:
            c = 0
            del lst[i]
        else:
            i += 1
        if i >= len(lst):
            i = 0
    # print(lst)
    return lst[0]

# 也会超时。。。
def josephus_survivor_b(n,k):
    #your code here
    lst = list(range(1, n+1))
    l = len(lst)
    i = 0
    c = 1
    s = l
    while s > 1:
        if c == k:
            s -= 1
            c = 0
            lst[i] = 0
        i += 1

        if i >= l:
            i = 0
        if lst[i] != 0:
            c += 1
    res = -1
    for i in lst:
        if i != 0:
            res = i
    # print(res)
    return res

# GeekforGeek的递归版，会导致栈溢出
def josephus_survivor_rev(n,k):
    if (n == 1):
        return 1
    else:
        # The position returned by
        # josephus(n - 1, k) is adjusted
        # because the recursive call
        # josephus(n - 1, k) considers
        # the original position
        # k%n + 1 as position 1
        return (josephus_survivor(n - 1, k) + k - 1) % n + 1


# 通过， GeekforGeek 迭代版
def josephus_survivor(n, k):
    s = 0
    for i in range(2, n+1):
        s = (s + k) % i
        print(s)
    return s + 1

# 通过，https://xbuba.com/questions/12444979
def josephus(n, k):
    ls = list(range(1, n+1))
    k -= 1  # pop automatically skips the dead guy
    if n > k:
        idx = k
    else:
        idx = k % n
    print(ls)
    while len(ls) > 1:
        print(ls.pop(idx))  # kill prisoner at idx
        idx = (idx + k) % len(ls)
    # print(ls)
    return ls[0]

# print(f'res {josephus(14, 2)}')
print(f'res {josephus(11, 19)}')
# 1, 2, 3