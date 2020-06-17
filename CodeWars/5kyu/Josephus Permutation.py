"""
k >= 1
n: 1 to n

[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
[1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
[1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
[1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
[1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
[4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
[] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]
final result : josephus([1,2,3,4,5,6,7],3)==[3,6,2,7,5,1,4]
"""


def josephus(items,k):
    suicide = []
    ns = len(items)
    last = ns
    count = 0
    index = 0
    res = []
    while last > 0:
        if index not in suicide:
            count += 1
            if count > k:
                count = 1
        if count == k and index not in suicide:
            suicide.append(index)
            last -= 1
        index = (index + 1) % ns
    for i in suicide:
        res.append(items[i])
    print(res)
    return res

# =======大神解法

def josephus2(xs, k):
    i, ys = 0, []
    while len(xs) > 0:
        i = (i + k - 1) % len(xs)
        ys.append(xs.pop(i))  # 看起来 pop 方法完全符合这个问题：从 list 中删除指定位置元素并返回
    return ys

josephus([1,2,3,4,5,6,7],3)
