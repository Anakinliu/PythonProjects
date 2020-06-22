"""
螺旋数

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
"""


# 两年了还没进步 ：p
def snail(snail_map):
    n = len(snail_map)
    if n == 1:
        return snail_map[0]
    count = 0
    res = []
    direction = 'r'
    cir = 0
    while count < n * n - n:
        if direction == 'r':
            i = cir
            for j in range(cir, n - cir):
                res.append(snail_map[i][j])
            direction = 'd'
        if direction == 'd':
            j = n - cir - 1
            for i in range(cir + 1, n - cir):
                res.append(snail_map[i][j])
            direction = 'l'
        if direction == 'l':
            i = n - cir - 1
            for j in range(n - cir - 2, cir - 1, -1):
                res.append(snail_map[i][j])
            direction = 'u'
        if direction == 'u':
            j = cir
            for i in range(n - cir - 2, cir, -1):
                res.append(snail_map[i][j])
            direction = 'r'
            cir += 1
        print(res)
        count += 1
    # print(res)
    return res


# snail([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])


# MMMAAANNN, ruoyuchen, Alexkington, leodowhat, olivinepeng, Decimo (plus 8 more warriors)
def snail2(array):
    a = []
    while array:
        # 把序列加入list
        a.extend(list(array.pop(0)))
        # 列变行
        array = list(zip(*array))
        print(array)
        array.reverse()
    return a

#user7657844, AlexisBash, 5hy0w1, MARAL1365, nochkasl, monkeynuggets (plus 2 more warriors)
import numpy as np

def snail3(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m


array = [
    [1, 2, 3, 1],
    [4, 5, 6, 4],
    [7, 8, 9, 7],
    [7, 8, 9, 7]
]
snail2(array)
