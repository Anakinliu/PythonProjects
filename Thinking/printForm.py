
"""打印给定行数和列数的表格"""


def print_form(row, col):
    row = row * 5 + 1
    col = col * 5 + 1
    for r in range(row):
        if r % 5 == 0:
            for c in range(col):
                if c % 5 == 0:
                    print '+'  # 结尾不用默认的end='\n' 而是end=' '
                else:
                    print '-'
            print()
        else:
            for c in range(col):
                if c % 5 == 0:
                    print '|'
                else:
                    print ' '
            print()


print_form(4, 1)
