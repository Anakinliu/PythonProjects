"""
给定一组不同的整数nums，返回所有可能的子集（幂集）。
注意：解决方案集不得包含重复的子集。
EXAMPLE
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


# 手机APP给的迭代解法版解答
def subsets(nums):  # 数字列表
    nb_subsets = 2 ** len(nums)
    all_subsets = []

    for subset_nb in range(nb_subsets):
        subset = []
        print(subset_nb)  # 0 ~ 7
        for num in nums:  # 遍历裂变所有数字
            if subset_nb % 2 == 1:  # subset_nb是奇数
                subset.append(num)
            subset_nb = subset_nb // 2
        print(subset_nb)  # always be 0
        all_subsets.append(subset)
    return all_subsets

    pass


# print(subsets([1, 2, 3]))


# leetcode 讨论区 回溯解法 https://leetcode.com/problems/subsets/discuss/360873/Python-Backtracking
def solution(nums_lst):
    def explore(chosen, remaining, res):
        if not remaining:
            res.append(chosen[:])
            return
        d = remaining.pop(0)
        # choose
        chosen.append(d)
        # explore
        explore(chosen, remaining, res)
        chosen.pop()
        explore(chosen, remaining, res)
        # unchoose
        remaining.insert(0, d)

    result = []
    chosen = []
    explore(chosen, nums_lst, result)
    return result


print(solution([1,2,3]))

# 也是回溯解法
"""
level 0: []
level 1: [11]                    [22]       [33]
level 2: [11,22]     [11,33]     [22,33] 
level 3: [11,22,33]

"""
def subsets2(nums):
    res = []
    backtracking(res, 0, [], nums)
    return res


def backtracking(res, start, subset, nums):
    res.append(list(subset))
    for i in range(start, len(nums)):
        subset.append(nums[i])
        backtracking(res, i + 1, subset, nums)
        # print(subset.pop())


# print(subsets2([1, 2, 3]))
