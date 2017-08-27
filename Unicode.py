x = chr(92)
print(x)

# ord()与chr()功能相反

x = ord("[")
print(x)

# Python对bytes类型的数据用带前缀b的字符串表示,
# bytes类型是以字节为单位的，传输到网络或者磁盘上需要使用字节流

y = b'AFG'

# 此时bytes类型中的每个字符只占用一个字节

print(type(y))

print('中文'.encode('utf-8'))

# Python的默认编码是Unicode，
# 此时str类型可以通过encode()方法编码为bytes类型

e = '中文'.encode('utf-8')

print(e)

print(type(e))

# 反过来，如果从网络或者磁盘上读取字节流，
# 就需要把bytes类型转换成str，就要用decode()方法

print(e.decode('utf-8'))

# len()计算字符长度

# 对str计算包含字符数
print(len('attention'))

# 对bytes计算字节数
print(len(e))

# Python的格式化方式类似C语言，用%实现

print("%s\'s score is %06d" % ("Tom", 59))

# 如果你不太确定应该用什么，
# %s永远起作用，它会把任何数据类型转换为字符串

print("%-3s%s%s" % (5, 9.9, "快"))

# 当然，如果%就是用作普通字符，不用\；来转义，而是用%%表示

print("%d %%" % 100)

print("100%")


