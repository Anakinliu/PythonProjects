# Python内置的一种数据类型是列表：list。
# list是一种有序的集合，可以随时添加和删除其中的元素。

computers = ["first", 3, 4, "sd"]

print(type(computers))

print(len(computers))

print(type(computers[3]))

# 与已经学过的语言一样，用索引来访问list中每一个位置的元素

computers[3] = 666

print(computers[3])

# 可以修改list的元素的类型

print(type(computers[3]))

# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引

print(computers[-1])

print(computers[-4])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾

computers.append("addOne")

print("latest: " + computers[-1])

# 从列表末尾删除数据，返回此数据

pop = computers.pop()

# extend()用于在列表末尾增加一个  数据项  集合
# 如果不是数据项，而是单个元素，会把他拆开

computers.extend("new computer")  # 字母被拆分

computers.extend(["new"])   # 正常

print(computers)

# remove()方法用于移除指定的数据项

computers.remove("new")

# insert()方法用于在指定位置  之前  增加一个数据项
# 如果插入集合会有警告

computers.insert(7, "mmm")

print(computers)

# list查找较dict慢,属于线性查找，list越大，查找越慢

d = {'kim': 60, 'kill': 66, 'file': 80}

# dict根据关键字查找其对应的键值，因此关键字和键值有一一对应的关系


print(d["file"])

# 关键字相同可能会出意想不到的错误,现在出现较新的键值对覆盖了旧的

print(d)

d['fuck'] = "def"

print(d)

# 为啥每次相同的dist输出的元素顺序不一样！？
# dict对元素的顺序没有固定要求

# 输出字典可打印的字符串表示。

print(str(d))

但是 = 99

print(但是)
