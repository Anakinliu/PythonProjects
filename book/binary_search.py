# coding: utf-8
# 二分搜索


def main_fun(source, target):
    """
    source -> 有序列表
    target -> 查找目标

    找到目标就返回列表索引, 否则返回None

    """
    low = 0
    high = len(source) - 1

    while low <= high:
        mid = (low + high) // 2  # python3地板除取整
        if target == source[mid]:
            return mid
        if target < source[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


test_list = [1, 2, 4, 6, 22, 34, 55, 99, 192, 435, 999]
result = main_fun(test_list, 435)
print result
