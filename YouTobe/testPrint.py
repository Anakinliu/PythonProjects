a = "A"


# 注意这个 r !!
print(r"UF \b \n" + a)

# 数学运算 * 可以实现原地复制string
print("a * 6 : " + a * 6)

b = "liu yin quan" + "!"

# 截取字符串,起始位置与结束位值可省略,实际结束位值其实是结束值减去一!
print(b[0:12])

print(b[:3])

print(b[4:])


name_len = len(b)

print("My name's length is: " + str(name_len))


