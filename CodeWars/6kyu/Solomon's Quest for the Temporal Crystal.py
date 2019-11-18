# Python没有switch，网上都用的字典
def switch(e, coord, level_now):
    functions = {
        0: [coord[0], coord[1] + level_now * e[2]],
        1: [coord[0] + level_now * e[2], coord[1]],
        2: [coord[0], coord[1] - level_now * e[2]],
        3: [coord[0] - level_now * e[2], coord[1]],
    }
    return functions.get(e[1])

def solomons_quest(arr):
    coordinate = [0, 0]
    level_now = 0
    for e in arr:
        level_now = level_now + e[0]
        coordinate = switch(e, coordinate, 2**level_now)

    return coordinate


map_example = [[1,3,5],[2,0,10],[-3,1,4],[4,2,4],[1,1,5],[-3,0,12],[2,1,12],[-2,2,6]]
solomons_quest(map_example)

# @falsetru
def solomons_quest_2(arr):
    level = 0
    # 构思很巧妙，用的复数的实部虚部作为x与y
    ds = [1j, 1, -1j, -1]
    pos = 0
    for level_shift, direction, distance in arr:
        level += level_shift
        pos += (2**level) * (ds[direction] * distance)
    return [int(pos.real), int(pos.imag)]

# @Blind4Basics
# 巧妙利用了False和True作为序列索引！！！
def solomons_quest_3(arr):
    pos, lvl = [0,0], 0
    for dilat,dir,dist in arr:
        lvl += dilat
        pos[dir in [0,2]] += dist * 2**lvl * (-1)**( dir in [2,3] )
    return pos
lst = [2,5]
print(lst[False])
