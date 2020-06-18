"""
返回比给定数值更大一点的数，没有则返回 -1

12 ==> 21
513 ==> 531
2017 ==> 2071
"""

"""
 commit: 4KYU 是一个新世界啊！！！
"""


def permutations(arr, position, end, res=[]):
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


next_bigger2(122)
#
# arr = ["1","2","2"]
# res = []
# permutations(arr, 0, len(arr), res)
# print(res)


# import itertools
#
# def next_bigger(n):
#     all = []
#     n_str = str(n)
#     lst = list(n_str)
#     len_ = len(lst)
#     res = list(itertools.permutations(lst, len_))
#     bigger = -1
#     for i in res:
#         num = int(''.join(list(i)))
#         if num > n:
#             bigger = num
#             break
#     print(bigger)
#     return bigger
#
#
# next_bigger(123)