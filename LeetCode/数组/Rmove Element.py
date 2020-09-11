"""
给定数组和值v，原地移除值v并返回数组新长度
不要分配新的数组空间，必须原地操作数组
数组内元素顺序变化是可接受的

数组内新长度之外的元素会被忽略

"""
def removeElement(nums, val):
    nums_len = len(nums)
    idx = nums_len - 1
    i = 0
    count = 0
    while i < nums_len:
        if val == nums[i]:
            count += 1
            if nums[idx] != val:
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i -= 1
            idx -= 1
        if i == idx:
            break
        i += 1
    # print(nums)
    # print(nums_len - nums.count(val))
    # return nums_len - nums.count(val)
    return nums_len - count
    pass

def removeElement_two_pointer(nums, val):
    nums_len = len(nums)
    i = j = 0
    while j < nums_len:
        if nums[j] == val:
            j += 1
            continue
        else:
            nums[i] = nums[j]
            i += 1
            j += 1
    # print(nums)
    # print(i)
    return i
    pass

def removeElement_reduce_movement(nums, val):
    nums_len = len(nums)
    i = 0
    n = nums_len
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
    print(nums)
    print(n)
    return n
    pass

# nums = [0,1,2,2,3,0,4,2]
nums = [2, 0, 0, 2, 3, 2, 2, 2, 2, 2, 0, 2, 1, 3, 2, 2, 1, 3]
removeElement_reduce_movement(nums, 2)