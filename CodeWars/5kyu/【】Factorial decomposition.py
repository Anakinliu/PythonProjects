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
print(fact(14))
print(2**37 * 3**22 * 5 * 7 * 11 * 13)
# print(fact(5))
def decomp(n):
    factorial = fact(n)
    # 累乘结果
    m = 1
    res_str = []
    for base in prime(n):
        power = 1
        while base ** power + m <= factorial:
            power += 1
        print(base, power)
        m *= base ** (power - 1)
        if power == 1:
            res_str.append('{}'.format(base))
        else:
            # power > 1
            res_str.append('{}^{}'.format(base, power))
        if m == n:
            break
    print(' * '.join(res_str))
    return' * '.join(res_str)


decomp(22)