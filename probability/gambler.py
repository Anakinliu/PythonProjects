import random

"""TODO: 更多人分赌本, 各人的胜率不同"""

"""胜利n局是赢家, 两个人游戏, 每局的胜率都是1/2, 两人分别已经胜利了n1, n2局"""


def gambler(n, n1, n2):
    for i in range(2 * n - n1 - n2 - 1):
        win_prob = random.randint(0, 1)
        if win_prob == 0:
            n1 += 1
        else:
            n2 += 1
        if n1 == n:
            break
        if n2 == n:
            break
    print("n1: " + str(n1) + " " + "n2: " + str(n2))
    if n1 > n2:
        return 1
    else:
        return 2

s = 3
n1 = 2
n2 = 1
n1_win_count = 0
n2_win_count = 0
total_count = 10000

for i in range(total_count):
    who = gambler(s, n1, n2)
    if who == 1:
        n1_win_count += 1
    else:
        n2_win_count += 1

print("总共" + str(total_count) + "局")
print("玩家1赢的次数: " + str(n1_win_count))
print("玩家2赢的次数: " + str(n2_win_count))
