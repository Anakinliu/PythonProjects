"""
nums内元素有重复的
"""

# DFS递归调用解法
def subsetsWithDup2(nums):
    ret = []
    dfs(sorted(nums), [], ret)
    return ret


def dfs(nums, path, ret):
    ret.append(path)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        dfs(nums[i + 1:], path + [nums[i]], ret)

# 其他解法
def subsetsWithDup(nums):
    if not nums:
        return []
    nums.sort()  # 排序，
    res, cur = [[]], []
    for i in range(len(nums)):
        # 列表加列表就是追加元素
        if i > 0 and nums[i] == nums[i - 1]:
            cur = [item + [nums[i]] for item in cur]
        else:
            cur = [item + [nums[i]] for item in res]
        res += cur
    return res


print(subsetsWithDup2([1, 2, 2]))
