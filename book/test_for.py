# coding: utf-8
sf = []  # 空列表
for i in range(1, 11):
    square = i ** 2
    sf.append(square)

print (sf)
sf = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print (min(sf))  # 最大值
print (max(sf))  # 最小值
print (sum(sf))  # 求和