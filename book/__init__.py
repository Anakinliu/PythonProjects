# -*- coding: utf-8 -*-
print ("ABC".title())

# owewr和upper很有用, 可以把用户的不规范输入规范化

print ("aBC".lower())
print ("Abc".upper())

x = " sdsd "
print ((x.rstrip())) # 返回无尾端空格的字符串
# 头部空格使用lstrip
# 前后所有使用strip()

print ("i say \"sss\"" + "\n66666\t6666\tskdhsdkjsh\t\nssdd\t777\tssd")

print (3 / 2)

x = 100
print (r"my  favorite number is " + str(x))

y = [1, 2, 3]

print (y)

print (y[-1])
print (y[-2])

strlist = [1, "liu", "lao"]
print (len(strlist))
print (strlist[2])

strlist.append("233")
print (len(strlist))
print (strlist)

t = strlist.insert(0, 666)
print (len(strlist))

del strlist[3]

print (strlist)
strlist.pop()
x = strlist.pop(0)
print ("===============")
strlist.append(1)
print (strlist)
strlist.remove(1)
print (strlist)


