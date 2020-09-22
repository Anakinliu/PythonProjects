"""
您正在爬楼梯。
它需要n步才能到达顶部。
每次您可以爬1或2步。
您可以通过几种不同的方式登顶？
EXAMPLE
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45

输入阶梯个数，输出登顶方式数
"""

# 暴力递归版 n==35超时
def climb_stairs(n):
    if n == 0:
        return 1
    amount = 0
    for step in range(1, 3):
        if n - step < 0:        # 多走了
            continue
        amount += climb_stairs(n - step)
    return amount


# 备忘录版，去除冗余子问题
def climb_stairs2(n, n_lst):
    if n_lst[n]:
        return n_lst[n]
    if n == 0:
        return 1
    amount = 0
    for step in range(1, 3):
        if n - step < 0:  # 多走了
            continue
        amount += climb_stairs2(n - step, n_lst)
    n_lst[n] = amount
    return amount

# 动态规划版不写了，就是斐波那契额数
# print(climb_stairs(2))
lst = [0] * 45
print(climb_stairs2(6, lst))
