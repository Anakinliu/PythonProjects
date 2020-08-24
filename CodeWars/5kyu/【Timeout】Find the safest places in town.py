"""
劳拉·巴西（Laura Bassi）是欧洲大学的第一位女教授。
尽管她的智力很高，但并不总是允许她公开演讲。
有一天，一位在学术界对妇女抱有非常强烈反对信念的教授派遣了一些特工找到了Bassi，
并结束了她的职业生涯。
你需要告诉她镇上最安全的地方，帮助她逃脱！

TASK

agents 是一个数组，表示特工的坐标
n Bassi所在城市的方格的边长

举例：
n = 6
agents = [(0,0),(1,5),(5,1)]

方格：数字代表与最近的特工距离
0 1 2 3 2 1
1 2 3 2 1 0
2 3 4 3 2 1
3 2 3 4 3 2
2 1 2 3 4 3
1 0 1 2 3 4
最安全的空间是距离4，因此该函数应返回[（2，2），（3，3），（4，4），（5，5）]
返回的list没有顺序
PS
1. 如果每个网格单元上都有一个代理，则没有安全空间，因此请返回一个空列表。
2. 如果没有特工，则每个单元格都是安全的空间，因此返回所有坐标。
3. n = 0，返回空list
4. 如果特工坐标不在地图内，则根本不考虑它们。
5. 没有重复的特工
6. 所有参考解决方案的运行时间约为6秒。
如果使用暴力解决方案，则可能无法通过测试。
有200个随机测试，其中n <=50。低效的解决方案可能会超时。
"""
import math


def advice(agents, n):
    """
    :param agents: 特工的坐标 index
    :param n: town的边长，正方形
    :return: 安全位置
    """
    if n == 0:
        return []
    town_lst = [[-1 for j in range(n)] for i in range(n)]
    agents = [e for e in agents if 0 <= e[0] < n and 0 <= e[1] < n]
    if agents:
        for r in range(n):
            for c in range(n):
                if town_lst[r][c] != 0:
                    town_lst[r][c] = min(
                        [abs(r - agent[0]) + abs(c - agent[1]) for agent in agents if 0 <= agent[0] < n and 0 <= agent[1] < n])
    # print(town_lst)
    max_v = max([max(i) for i in town_lst])
    # print(max_v)
    # print([(i, j) for j in range(n) for i in range(n) if town_lst[i][j] == max_v])
    if max_v == 0:
        # returns empty list for agents everywhere
        return []
    elif max_v == -1:
        return [(i, j) for j in range(n) for i in range(n)]
    else:
        return [(i, j) for j in range(n) for i in range(n) if town_lst[i][j] == max_v]
    # print(result)
    pass


# advice([(0, 0), (1, 5), (5, 1)], 6)
# advice([(1, 1), (1, 0), (0, 0), (0, 1)], 2)
print(advice([(9, 9)], 1))
# advice([(0, 0), (1, 1), (99, 99)], 2)