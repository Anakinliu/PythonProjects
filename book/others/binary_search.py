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
    times = 0
    print('比较次数: ', end="")
    while low <= high:
        # 为什么是相加再除2? 其实
        mid = low + (high - low) // 2  # python3地板除取整
        if target == source[mid]:
            times += 1
            print(times)
            return mid
        times += 1
        if target < source[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print(times)
    return None


# test_list = [1, 2, 4, 6, 22, 34, 55, 99, 192, 435, 999]
big_test = []
for item in range(100):
    big_test.append(item)

result = main_fun(big_test, 99)
print('target index is : ' + str(result))
