"""
每一列，每一行以及9个3x3子网格（也称为块）中的每一个都包含从1到9的所有数字。
方法输入表示Sudoku board的 2D list，如果是有效的解决方案，则返回true，否则返回false。

数独板上的单元也可能包含0，代表空单元。
包含一个或多个零的board被视为无效解决方案。

棋盘总是9个单元格×9个单元格，每个单元格只包含从0到9的整数。

"""


def solution(board):
    # x = [0 in e for e in board]
    # print(x)
    # 判断是否包含 0
    if any([0 in e for e in board]):
        return False

    # 3*3 block
    for row in range(0, 7, 3):
        for col in range(0, 7, 3):
            res = set()
            x = {board[i][j] for i in range(row, row + 3) for j in range(col, col + 3)}
            # print(res)
            if len(x) != 9:
                return False

    # 行
    for row in range(9):
        if len(set(board[row][:])) != 9:
            return False

    # 获取列
    for col in range(9):
        x = [e[8] for e in board]
        if len(set(x)) != 9:
            return False
    return True
    pass


board2 = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
          [4, 9, 8, 2, 6, 1, 3, 7, 5],
          [7, 5, 6, 3, 8, 4, 2, 1, 9],
          [6, 4, 3, 1, 5, 8, 7, 9, 2],
          [5, 2, 1, 7, 9, 3, 8, 4, 6],
          [9, 8, 7, 4, 2, 6, 5, 3, 1],
          [2, 1, 4, 9, 3, 5, 6, 8, 7],
          [3, 6, 5, 8, 1, 7, 9, 2, 4],
          [8, 7, 9, 6, 4, 2, 1, 3, 5]]

board3 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
          [2, 3, 4, 5, 6, 7, 8, 9, 1],
          [3, 4, 5, 6, 7, 8, 9, 1, 2],
          [4, 5, 6, 7, 8, 9, 1, 2, 3],
          [5, 6, 7, 8, 9, 1, 2, 3, 4],
          [6, 7, 8, 9, 1, 2, 3, 4, 5],
          [7, 8, 9, 1, 2, 3, 4, 5, 6],
          [8, 9, 1, 2, 3, 4, 5, 6, 7],
          [9, 1, 2, 3, 4, 5, 6, 7, 8]]

# print(solution(board2))
print(solution(board3))
