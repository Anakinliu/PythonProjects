"""
给定一个整数列表，返回列表包含：元素可被整除的素数及这个素数与元素的倍数的和组成的新列表

Example:

I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:
所有元素和可能为 0

Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.
"""
from collections import defaultdict


def judge_prime(n):
    if n <= 1:
        return False
    for m in range(2, n//2 + 1):
        if n % m == 0:
            return False
    return True


def prime_gen(n):
    for i in range(2, n+1):
        if n % i == 0 and judge_prime(i):
            yield i


def solution(lst):
    dct = defaultdict(int)
    for e in lst:
        primes = [p for p in prime_gen(abs(e))]
        for k in primes:
                dct[k] += e
    # print(dct)
    res = []
    for k in sorted(dct.keys()):
        res.append([k, dct[k]])
    return res

# print([e for e in prime_gen(-45)]) # 空, 需要加绝对值
# print(-45 % 6)


solution([12, 15])
# solution([15, 21, 24, 30, 45])


# 大神解答区

def sum_for_list2(lst):
    # 集合生成式
    factors = {i for k in lst for i in range(2, abs(k)+1) if not k % i}
    print(factors)  # 2-lst[i]，所有可整除的数的集合

    # 从 factor 取出元素 i，需要元素 满足 ：factor除 i 外的元素都不能把 e 整数
    prime_factors = {i for i in factors if not [j for j in factors-{i} if not i % j]}
    print(prime_factors)

    # 列表生成式
    return [[p, sum(e for e in lst if not e % p)] for p in sorted(prime_factors)]


# sum_for_list2([12,15])