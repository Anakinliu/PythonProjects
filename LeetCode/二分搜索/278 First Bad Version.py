"""
您是产品经理，目前正在领导团队开发新产品。
不幸的是，您产品的最新版本未通过质量检查。
由于每个版本都是基于先前版本开发的，因此错误版本之后的所有版本也都是错误的。

假设您有n个版本[1、2，...，n]，并且您想找出第一个不良版本，这将导致随后的所有不良版本。

您将获得一个API :
bool isBadVersion（version）
它将返回版本是否错误。
实现一个函数：
查找第一个不良版本。

应尽量减少对API的调用。

"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    if version >= 2:
        return True
    else:
        return False
    pass

# 我写的递归版
def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """

    def do(left, right):
        if isBadVersion(left):
            return left
        if left >= right:
            return left
        middle = left + (right - left) // 2
        if isBadVersion(middle):
            left += 1
            right = middle
            return do(left, right)
        else:
            left = middle + 1
            return do(left, right)
    return do(1, n)


print(firstBadVersion(2))

# 讨论区的迭代版
def firstBadVersion2(n):
    i = 1
    j = n
    while i < j:
        k = (i + j) // 2
        if isBadVersion(k):
            j = k
        else:
            i = k + 1
    return i
