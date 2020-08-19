"""
拆分所有乘数为素数相乘的形式
"""
print('OK')
# 先计算阶乘的结果
def fact(n):
    i = 1
    result = 1
    while i <= n:
        result *= i
        i += 1
    return result


def judge_prime(n):
    if n <= 1:
        return False
    for m in range(2, n//2 + 1):
        if n % m == 0:
            return False
    return True

#
# for i in range(100):
#     if judge_prime(i):
#         print(i)


def prime(n):
    for i in range(n+1):
        if judge_prime(i):
            yield i


# for x in prime(5):
#     print(x)
# print(fact(14))
# print(2**37 * 3**22 * 5 * 7 * 11 * 13)
# print(fact(5))


def not_prime(n):
    """
    :param n: 非素数整数
    :return: 一组素数列表，乘积 == n
    """
    start = 0
    primes = [e for e in prime(n)]
    res = []
    while judge_prime(n) is False:
        if n % primes[start] == 0:
            res.append(primes[start])
            n = n // primes[start]
        else:
            start += 1
    res.append(n)
    # print(res)
    return res


# not_prime(9)


def decomp(n):
    factorial = fact(n)
    # 累乘结果
    lst = []
    dct = dict()
    for i in range(2, n+1):
        if judge_prime(i):
            lst.append(i)
            dct[i] = 1
        else:
            lst.extend(not_prime(i))
    for k in dct.keys():
        dct[k] = lst.count(k)
    res_lst = []
    for k, v in dct.items():
        if v == 1:
            res_lst.append('{}'.format(k))
        else:
            res_lst.append('{}^{}'.format(k, v))
    # print(lst)
    # print(dct)
    res_str = ' * '.join(res_lst)
    print(res_str)
    return res_str

# "2^95 * 3^46 * 5^22 * 7^16 * 11^8 * 13^7 * 17^5 * 19^5 * 23^4 * 29^3 * 31^3 * 37^2 * 41^2 * 43^2 * 47^2 * 53 * 59 * 61 * 67 * 71 * 73 * 79 * 83 * 89 * 97"


decomp(98)