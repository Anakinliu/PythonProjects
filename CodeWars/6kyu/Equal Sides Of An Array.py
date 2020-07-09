"""
一组整数，返回索引，此索引左半边的数的和等于右半边的和
多个N满足条件时，小的优先，空数组==0
"""
def find_even_index(arr):
    # if sum(arr) == 0:
    #     return 0
    # if sum(arr[1:]) == 0:
    #     return 0
    # if len(arr) == 1:  # [x]
    #         return 0
    result = -1
    for idx in range(len(arr)):  # [x,y]
        if sum(arr[:idx]) == sum(arr[idx+1:]):
            result = idx

            # print(idx)
    return result

# zebulan, sriddle, prashanth041, asir2-16, Anubhab_code, OlegSanders
# 先计算和，然后开始扫描
def find_even_index_clever(lst):
    left_sum = 0
    right_sum = sum(lst)
    for i, a in enumerate(lst):
        right_sum -= a
        if left_sum == right_sum:
            return i
        left_sum += a
    return -1


lst = [2,4,6,8,10]
# print(lst[1:1])
find_even_index([])

print(lst[-2:0:-2])