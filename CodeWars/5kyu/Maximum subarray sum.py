"""

最简单的情况是，列表仅由正数组成，最大和为整个数组的和。
如果列表仅由负数组成，则返回0。
空列表被认为具有零最大和。
请注意，空列表或数组也是有效的子列表/子数组。
"""
def max_sequence(arr):
    if arr:
        if max(arr) < 0:
            return 0
        max_sub = arr[0]
        len_arr = len(arr)
        for i in range(len_arr-1):
            for j in range(i+1, len_arr+1):
                s = sum(arr[i:j])
                print(s)
                if s > max_sub:
                    max_sub = s
        return max_sub
    else:
        return 0


def maxSequence2(arr):
    lowest = ans = total = 0
    for i in arr:
        total += i
        lowest = min(lowest, total)
        ans = max(ans, total - lowest)
    return ans


print(maxSequence2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))