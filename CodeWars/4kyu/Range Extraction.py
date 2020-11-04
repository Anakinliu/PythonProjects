"""
给定一串整数，返回格式化后的：
如果有 3 个或以上的整数是连着的，则用start-end表示，包括start和end。

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"

整数列表以递增顺序传入。
"""


def solution(lst):
    # 模仿solution2，假加入一个必定不满足条件的元素！
    lst.append(lst[-1]+2)
    stack = []  # 放入元素，如果后续元素与前面的元素的差值不为 1，则弹出前面的元素
    res = []
    stack_top = -1
    # stack_bottom = -1
    while lst:
        ele = lst.pop(0)
        stack.append(ele)
        stack_top += 1
        if ele - stack[stack_top - 1] > 1:
            if len(stack) - 1 >= 3:
                res.append(f'{stack[0]}-{stack[-2]}')
            else:
                while len(stack) > 1:
                    res.append(str(stack.pop(0)))
            stack = [stack[-1]]
            stack_top = 0
    # 因为lst最后一个数与前面的数可能是连着的，所以需要再看stack还有没有数
    # if stack:
    #     if len(stack) >= 3:
    #         res.append(f'{stack[0]}-{stack[-1]}')
    #     else:
    #         while stack:
    #             res.append(str(stack.pop(0)))
    # print(res)
    # print(','.join(res))
    return ','.join(res)


def solution2(args):
    out = []
    # begin和end之间组成的list相当于上面的stack
    beg = end = args[0]

    # args[1:] + [""]：这样就不用我的那个笨方法了，还要最后判断stack里的数，直接在原args里加一个，加的那最后一个数不满足“条件”即可！
    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:  # 是“单个数”
                out.append(str(beg))
            elif end == beg + 1:  # 是“连续的两个数”
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)


test = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
print(solution2(test))
print(solution(test))
