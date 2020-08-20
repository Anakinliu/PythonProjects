"""
输入
数据由一个包含至少一个名称的数组和一个整数n组成，
该整数可能与您选择的语言支持的最大数字一样高（当然，如果有这种限制）。
输出
喝第n罐可乐的人的名字。

1 Sheldon, Leonard, Penny, Rajesh, Howard
2 Leonard, Penny, Rajesh, Howard, Sheldon, Sheldon
3 Penny, Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard
4 Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
"""
def who_is_next(names, r):
    len_names = len(names)
    n = 0  # 第几次循环
    result = len_names * n
    while result < r:
        result += len_names * 2 ** n
        n += 1
        pass
    print(n, result)  # 第几次循环
    idx = len_names - int(((result - r) // 2 ** (n - 1))) - 1
    print(idx)
    print(result, r, n, len_names * 2 ** n)
    return names[idx]


# 答案区
def who_is_next_plus(names, r):
    index = r - 1
    l_names = len(names)

    while index >= l_names:
        # skip the beginning and de-duplicate pairs, e.g.:
        # 跳过开始的第一个和重复的（Double）
        # 'abcaabbcc'[5] == 'aabbcc'[5 - 3] == 'abc'[(5 - 3) // 2]
        index = (index - l_names) // 2

    return names[index]

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "GG"]

# who_is_next(names, 1)
# who_is_next(names, 13)
# who_is_next(names, 1)  # "Sheldon"
who_is_next(names, 52)  # "Penny"
# who_is_next(names, 7230702951)  # "Leonard"

