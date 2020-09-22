"""
求第 N 个斐波那契额数
"""
# STEP 1 暴力递归
def fib1(N):
    if N == 1 or N == 2:
        return 1
    return fib1(N - 1) + fib1(N - 2)

# print(fib1(12))  # 144

# STEP 2 带备忘录的递归解法
def fib2(N):
    if N == 1 or N == 2:
        return 1
    mono = [0] * (N + 1)
    print(mono)
    mono[1] = mono[2] = 1
    result = do(N, mono)
    print(mono)
    print(result)


def do(N, mono):
    # 已经设置条件 mono[1] = mono[2] = 1
    if mono[N] != 0:
        return mono[N]
    # 先保存值
    mono[N] = do(N-1, mono) + do(N-2, mono)
    # 在返回结果给上一级调用
    return mono[N]

fib2(12)  # 144
