# 1. C cat D dog m mouse
# 2. cat caught mouse in j step
# 3. step is a "."
# 4. cat cannot jump over Dog
import math


def cat_mouse(x, j):
    try:
        dog_pos = x.index('D')
        cat_pos = x.index('C')
        mouse_pos = x.index('m')
        print(dog_pos, cat_pos, mouse_pos)
        if abs(mouse_pos - cat_pos) > j+1:
            return 'Escaped!'
        if (mouse_pos < dog_pos < cat_pos
                or cat_pos < dog_pos < mouse_pos):
            return 'Protected!'
        return 'Caught!'

    except ValueError:
        return 'boring without all three'
    pass

# codewar user
def cat_mouse2(x,j):
    c, m, d = x.find('C'), x.find('m'), x.find('D')
    if -1 in (c, m, d):
        return 'boring without all three'
    print(c, m, d)
    if abs(c - m) <= j+1:
        return 'Protected!' if c < d < m or c > d > m else 'Caught!'
    return 'Escaped!'


print(cat_mouse2('..............C.....m..D...',
                5))
