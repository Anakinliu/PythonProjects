from random import randint

x = int(input('输入你猜的数字：(0~100)'))
choice = 1
ran = randint(0, 100)
print(ran)
while choice < 10 and x != ran:
    if x != ran:
        choice += 1
        if x < ran:
            x = int(input('oops! 太小了，再来：(0~100)'))
        if x > ran:
            x = int(input('太大了！：(0~100)'))

print('你用了%d次猜对了' % choice)