"""
https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6
"""
def digital_root(n):
    str_n = str(n)
    result = n
    while len(str_n) != 1:
        result = 0
        for i in str_n:
            result += int(i)
        str_n = str(result)
    return result

# 大神解法
def digital_root2(n):
    # map函数：把int应用到可迭代对象的每一个元素上，返回的也是一个可迭代对象
    return n if n < 10 else digital_root(sum(map(int,str(n))))

# print(digital_root(456))
