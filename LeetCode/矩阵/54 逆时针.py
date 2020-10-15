"""
给定一个m x n元素的矩阵（m行，n列），以螺旋顺序返回矩阵的所有元素。
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

"""


def solution(matrix):
    if matrix:
        # m为行数
        # n为列数
        m, n = len(matrix), len(matrix[0])
        loop = 0
        # directions = [0, 1, 2, 3]
        output = []
        direction = 0
        while len(output) < m * n:
            print(f'{len(output)}------------')
            if direction == 0:
                for h in range(loop, m - loop):
                    output.append(matrix[h][loop])
                direction = 1
                print('0 done')
                continue
            if direction == 1:
                for h in range(loop + 1, n - loop):
                    output.append(matrix[m - loop - 1][h])
                direction = 2
                print('1 done')
                continue
            if direction == 2:
                for h in range(m - loop - 2, loop - 1, -1):
                    output.append(matrix[h][n - loop - 1])
                direction = 3
                print('2 done')
                continue
            if direction == 3:
                for h in range(n-loop-2, loop, -1):
                    output.append(matrix[loop][h])
                direction = 0
                loop += 1
                print('3 done')
                continue
        print(output)
        return output
    pass


t = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
solution(t)
