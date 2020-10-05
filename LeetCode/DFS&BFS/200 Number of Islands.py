"""
给定二维地图“ 1”（土地）和“ 0”（水），计算岛屿的数量。
一个岛屿被水包围，是通过水平或垂直连接相邻的陆地而形成的。斜线不算相连的陆地。
您可以假定地图的所有四个边都被水包围。
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
注意输入的元素是str
"""

m = 0
n = 0
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))


def solution(grid):
    if not grid:
        return 0
    global m, n
    m = len(grid)
    n = len(grid[0])
    islands_num = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] != '0':
                dfs(grid, i, j)
                islands_num += 1
    return islands_num


def dfs(grid, i, j):
    if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] == '0':
        return
    grid[i][j] = '0'
    for direction in directions:
        dfs(grid, i + direction[0], j + direction[1])

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(solution(grid))