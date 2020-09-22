"""
题目：给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，再给一个总金额 n，
问你最少需要几枚硬币凑出这个金额，如果不可能凑出，则回答 -1 。
"""
INT_MAX = 9999
enable_coins = [1, 2, 5]

# 暴力解法
def coinChange(coins, amount):
    if amount == 0:
        return 0
    ans = INT_MAX
    for coin in coins:
        # 金额不可达
        if amount - coin < 0:
            continue
        subProb = coinChange(coins, amount - coin)
        # 子问题无解
        if subProb == -1:
            continue
        ans = min(ans, subProb + 1)
    return -1 if ans >= INT_MAX else ans

# print(coinChange(coins, 11))


# 动态规划，加入一维动态规划数组
def coin_change_dp(coins, amount):
    dp = [INT_MAX] * (amount + 1)
    dp[0] = 0
    for jin_e in range(1, amount+1):
        for coin in coins:
            if coin <= jin_e:
                dp[jin_e] = min(dp[jin_e], dp[jin_e - coin] + 1)  # 关键 jin_e - coin
    print(dp)
    return -1 if dp[amount] > amount else dp[amount]


# print(coin_change_dp(enable_coins, 10))
