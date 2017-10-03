def main_fun(source, target):
    low = 0
    high = len(source) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == source[mid]:
            return mid
        if target < source[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


test_list = [1, 2, 4, 6, 22, 34, 55, 99, 192, 435, 999]
result = main_fun(test_list, 435)
print result
