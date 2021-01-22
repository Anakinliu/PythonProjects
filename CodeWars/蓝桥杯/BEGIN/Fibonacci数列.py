"""
输入n，输出第 n 个斐波纳挈数除以10007的余数。
"""
# n = input()
import line_profiler


@profile
def solution(n):
    n = int(n)
    if n == 1 or n == 2:
        print(1)
    a = 1
    b = 1
    s = 2
    for e in range(2, n):
        s = (a + b) % 10007
        a, b = b, s
    print(s)
    # return s


solution(99999)