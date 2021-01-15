"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0
编写一个采用数组并将所有零移动到末尾的算法，同时保留其他元素的顺序。
move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
"""
"""

"""


def move_zeros(array):
    # your code here
    # count = 0
    # print(array)
    for i, e in enumerate(array):
        if (e == 0 or e == 0.0) and not isinstance(e, bool):
            pre = i
            for j in range(i, len(array) - 1):
                if (array[j + 1] != 0 or array[j + 1] != 0.0) or array[j+1] is False:
                    array[pre], array[j + 1] = array[j + 1], array[pre]
                    pre = j + 1
                # count += 1
        # print(array)
    # print(array)


# move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"])
# move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9])
# ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 正解
# ['a', 'b', None, 'c', 'd', 1, 1, 3, [], False, 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ['a', 'b', None, 'c', 'd', 1, 1, 3, [], False, 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def move_zeros2(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

# sorded排序一个bool数组：
# x = [True,False,False,True]
# sorted(x)
# 结果：[False, False, True, True]