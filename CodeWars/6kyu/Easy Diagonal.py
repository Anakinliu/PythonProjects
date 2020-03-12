def diagonal(n, p):
    # your code
    n = n + 1
    matrix = []
    result = 0
    for i in range(n):
        row = [0 for _ in range(i+1)]
        row[0] = 1
        for j in range(1, i):
            row[j] = matrix[i-1][j] + matrix[i-1][j-1]
            if j == p:
                result += row[j]
                break
            pass
        row[-1] = 1

    return


def diagonal2(n, p):
    pass

# 129100 5
print(diagonal(20000, 40))


