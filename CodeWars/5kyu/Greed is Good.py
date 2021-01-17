"""
一种骰子游戏，有五个六面骰子。
您的任务是根据这些规则得分:
 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
您将始终得到一个包含五个六面骰子值的数组。
不能重复使用一个骰子计算分数
 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
"""


def score(dice):
    s = 0
    # 1,2,3,4,5,6
    d = [0, 0, 0, 0, 0, 0]
    points = [1000, 200, 300, 400, 500, 600]
    extra = [100, 0, 0, 0, 50, 0]
    for die in dice:
        d[die-1] += 1
    # guumaster, Powerful_Vadik, Tjofil, Brikarl, zhangjingwen2019, zhouzhenkaii, svetkolukk, starter727, wsa, AnastasiiaDemenkova (plus 1 more warriors)
    for idx, e in enumerate(d):
        s += points[idx] if e >= 3 else 0 + extra[idx] * (idx % 3)
    # print(d)
    # 使用points加extra不用加这些if了
    # for idx, c in enumerate(d):
    #     if c >= 3:
    #         if idx == 0:
    #             s += 1000
    #         else:
    #             s += (idx+1)*100
    #         if c > 3:
    #             if idx == 0:
    #                 s += 100 * (c - 3)
    #             if idx == 4:
    #                 s += 50 * (c - 3)
    #     else:
    #         if idx == 0:
    #             s += 100 * c
    #         if idx == 4:
    #             s += 50 * c
    #     pass
    # print(s)
    print(s)
    return s


# dice = [5, 1, 3, 4, 1]
# dice = [1,1,1,3,1]
dice = [2, 4, 4, 5, 4]
score(dice)