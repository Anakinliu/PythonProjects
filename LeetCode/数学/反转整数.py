# 注意反转后的整数的大小！！！
def reverse(x):
    y = x
    if y < 0:
        y = - y
    res = y % 10
    b = y // 10
    while b != 0:
        res = res * 10
        res += (b % 10)
        b = b // 10
    # print(res)
    res = res if x >= 0 else -res
    if res < -2**31 or res >= 2**31:
        return 0
    return res

print(reverse(-123))
print(reverse(9646324351))