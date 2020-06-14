"""
 @Description      
 @author          linux
 @create          2020-05-20 20:13
"""
"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
"""

# nums1: List[int], m: int, nums2: List[int], n: int
def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1 = m - 1  # nums1尾索引
    p2 = n - 1  # nums2尾索引
    p = m + n - 1  # 合并后的尾索引
    # c = 0
    while p1 >= 0 and p2 >= 0:
        # c += 1
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            # nums1[p], nums1[p1] = nums1[p1], nums1[p]
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    nums1[:p2 + 1] = nums2[:p2 + 1]  # p2大于等于0
    # print(c)
    # 因为nums1中比nums2大的都往后移了
    # 所以如果nums2中有剩余，可以直接放在nums1中
    return nums1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))
# lst = [1,2,0,4,3]
# lst.sort()
# print(lst)