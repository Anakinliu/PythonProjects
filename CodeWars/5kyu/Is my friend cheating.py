# https://www.codewars.com/kata/5547cc7dcad755e480000004/train/python

"""
TODO 做不出来。。
"""
def removNb(n):
    # your code
    result = []
    all_sum = 0
    for i in range(1, n+1):
        all_sum = all_sum + i
    # all_sum = sum((range(1, n+1)))
    print(all_sum)
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i * j == (all_sum - i - j):
                result.append((i, j))
                result.append((j, i))
    return result

print(removNb(26000000))