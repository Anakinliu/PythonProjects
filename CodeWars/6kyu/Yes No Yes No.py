"""

"""

def yes_no(arr):
    #your code here
    len_arr = len(arr)
    if len_arr == 0:
        return []
    if len_arr == 1 or len_arr == 2:
        return arr
    yn = [False for _ in range(len_arr)]
    yn[0] = True
    # print(yn)
    result = list()
    result.append(arr[0])
    j = 0
    for i in range(len_arr):
        j = (j + 1) % len_arr
        count = 0
        while count != 2:
            if yn[j] is False:
                count += 1
            if count == 2:
                break
            j = (j + 1) % len_arr
        result.append(arr[j])
        if len(result) == len_arr:
            break
        yn[j] = True
    # print(result)
    return result


# API，算法大佬的答案
from collections import deque

def yes_no2(arr):
    d, result = deque(arr), []
    while d:
        result.append(d.popleft())  # 弹出并删除最左端元素
        d.rotate(-1)  # 把最左边的1个元素放到最右边
    return result



# yes_no([1 , 2 , 3 , 4, 5 , 6 , 7 , 8, 9 , 10 ])
# yes_no(['this', 'code', 'is', 'right', 'the'])
# yes_no(["a"])
t = deque([1 , 2 , 3 , 4, 5 , 6 , 7 , 8, 9 , 10 ])

