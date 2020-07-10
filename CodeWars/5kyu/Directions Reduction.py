"""
四个方向，两个相反方向是紧挨时，无效操作，呆在原地
函数接收方向的字符串数组，返回字符串数组，去除无用方向

只有一个线程，直接list，不考虑多线程了，多线程可以使用queue试一下
"""

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]


def dirReduc(arr):
    dct = {'NORTH': 1, 'SOUTH': -1, 'EAST': 2, 'WEST': -2}
    lst = []
    for i in arr:
        if lst and dct[i] + dct[lst[-1]] == 0:
            lst.pop()
            continue
        lst.append(i)
    return lst


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

# Chrisi, BobrovAE308, Mario Montalvo, pitchet95, zhi_wang, Self Lee (plus 14 more warriors)
def dirReduc_clever(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc_clever(dir3) if len(dir3) < len(arr) else dir3


print(dirReduc_clever(a))

# test.assert_equals(dirReduc(a), ['WEST'])
