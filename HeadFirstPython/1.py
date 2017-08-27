comp = ['ww', 4, 'ss', 'ee']

print(comp)

s = comp.pop()

print(comp.pop())
print(s)

print(comp)

comp.append("aa")

comp.extend(["ww", "ss1", "ee1"])

print(comp)

comp.remove("ww")

print(comp)

comp.insert((len(comp) - 1), "rr")

print(comp)

# python列表可以包含混合类型的数据，可以混合存储任意数据

comp.insert(1, 0)

comp.insert(3, 0)

print(comp.index(0))

print(comp)

for com in comp:
    print(com)

games = [["GTA5", [2013, 2014, 2015]], ["cs"], "ssd"]

print("games : %s " % games)

print("games[0] : %s" % games[0])

# ！str数据类型也有下标 !

print("games[0][0][2] : %s" % games[0][1][2])

print("games[1] : %s" % games[1])

# isinstance(变量，类型)---判断变量是否是此类型

if isinstance(games, list):
    print("is")
else:
    print("no")

# 输出所有的built in function
# 即 BIF
# print(dir(__builtins__))

print()

for each_game in games:
    if isinstance(each_game, list):
        for each_game_2 in each_game:
            print(each_game_2)

    else:
        print(each_game)

# 循环太多怎么办？！
# 有太多重复的代码可不是好事！


