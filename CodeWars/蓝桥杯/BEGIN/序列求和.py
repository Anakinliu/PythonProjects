"""
1 <= n <= 1,000,000,000
输出 1 到 n 累加的和
"""
n = input()


def solution(x):
    x = int(x)
    print(x * (x + 1) // 2)


solution(n)
