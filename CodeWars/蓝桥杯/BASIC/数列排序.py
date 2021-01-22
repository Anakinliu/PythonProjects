"""
输入格式
　　第一行为一个整数n。
　　第二行包含n个整数，为待排序的数，每个整数的绝对值小于10000。
输出格式
　　输出一行，按从小到大的顺序输出排序后的数列。
样例输入
5
8 3 6 4 9
样例输出
3 4 6 8 9
"""
c = int(input())
ls = input().split(' ')
res = sorted([int(e) for e in ls])
for i in res:
    print(i, end=' ')
# print(' '.join(res))
# print(c)
# print(ls)
