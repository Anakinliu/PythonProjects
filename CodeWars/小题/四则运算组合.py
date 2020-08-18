"""
组合的方法是在各个数字之间插入四则运算的运算符组成算式，然
后计算算式的结果（某些数位之间可以没有运算符，但最少要插入 1 个
运算符）。
组合算式的计算结果为“将原数字各个数位上
的数逆序排列得到的数”，并且算式的运算按照四则运算的顺序进行
（先乘除，后加减）。

求位于1000~9999，满足上述条件的数
"""


def mulst(lst):
    res = 1
    for e in lst:
        res *= e
    # print(res)
    return res


ops = ["*", ""]
for n in range(1000, 10000):
    str_n = str(n)
    # 四位数，一共有 3 个空可以插入运算符
    lst_n = list(' '.join(list(str_n)))
    # print(lst_n)
    for i in ops:
        for j in ops:
            for k in ops:
                lst_n[1] = i
                lst_n[3] = j
                lst_n[5] = k
                if "" == i == j == k:
                    continue
                res = lst_n
                # print(res)  # ok
                sstr_n = ''.join(res)
                # print(sstr_n)  # ok
                llst_n = sstr_n.split('*')
                # print(llst_n)
                # print(str_n[::-1])
                if mulst([int(e) for e in llst_n]) == int(str_n[::-1]):
                    print(n)

print('---')
# print(int('001',10))