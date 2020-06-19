import time
# 输入两个n位的正整数, 都是str类型
"""
TODO 算法实现有问题，位数在递推后期不对
"""
def recMul(x, y):
    if len(x) == 1:
        print(x, y)
        return str(int(x) * int(y))
    int_1 = int(recMul(x[0:len(x) // 2], y[0:len(y) // 2]) + '0' * len(x))
    int_2 = int(str(int(recMul(x[0:len(x) // 2],  y[len(y) // 2:])) + int(recMul(x[len(x) // 2:],  y[0:len(y) // 2]))) + '0' * (len(x) // 2))
    int_3 = int(recMul(x[len(x) // 2:],  y[len(y) // 2:]))
    return str(int_1 + int_2 + int_3)

# s_t = time.time()
# print(recMul('567899999999', '123499999999'))
# print(time.time() - s_t)


def Karatsuba(x, y):
    print(len(x), len(y))
    if len(x) == 1:
        # print(x, y)
        return str(int(x) * int(y))
    else:
        a, b = x[0:len(x) // 2], x[len(x) // 2:]
        c, d = y[0:len(y) // 2], y[len(y) // 2:]
        p = int(a) + int(b)
        q = int(c) + int(d)
        int_ac = int(Karatsuba(a, c))
        int_bd = int(Karatsuba(b, d))
        int_pq = int(Karatsuba(str(p), str(q)))
        int_adbc = int_pq - int_ac - int_bd
        return str(int(str(int_ac) + '0' * len(x)) + int(str(int_adbc) + '0' * (len(x) // 2)) + int_bd)


print(Karatsuba('1234999912349999', '5678999956789999'))