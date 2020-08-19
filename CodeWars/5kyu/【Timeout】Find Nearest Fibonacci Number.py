"""
Given a positive integer (n) find the nearest fibonacci number to (n).
寻找距离 给定的正数 n 最近的 fib数
If there are more than one fibonacci with equal distance to the given number return the smallest one.
如果有多个距离 n 相等的数，返回最小的
Do it in a efficient way. 5000 tests with the input range 1 <= n <= 2^512 should not exceed 200 ms.

1 <= n <= 2^512， 要求时间小于 200ms
"""
import math
# 判断是否是 fib 数
def is_fib(number):
    if math.sqrt(5 * number ** 2 + 4) % 1 == 0.0 or math.sqrt(5 * number ** 2 - 4) % 1 == 0.0:
        return True
    return False
def nearest_fibonacci(number):
    # e1 = 1
    # e2 = 1
    # while not e1 <= number <= e2:
    #     e1, e2 = e2, e1 + e2
    #     # print(e1, e2)
    # e1_d = number - e1
    # e2_d = e2 - number
    # return e1 if e1_d <= e2_d else e2

    # N 是 Fibonacci number 当且仅当 ( 5*N^2 + 4 ) or ( 5*N^2 – 4 ) 是可以开根号得到整数的!

    if is_fib(number):
        return number
    else:
        c = 1
        while True:
            if is_fib(number - c):
                result = number - c
                break
            if is_fib(number + c):
                result = number + c
                break
            c += 1
    print(c)
    return result

# 求解第 n 个fib数
def fib(n):
    return round((((1+(5**0.5))/2)**int(n))/(5**0.5))

print(nearest_fibonacci(9))
# print(fib(7))