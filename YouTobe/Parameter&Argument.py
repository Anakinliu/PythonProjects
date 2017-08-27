import math

# 在函数内部,实参会赋值给形参


def print_thice(parameter):
    print(parameter)
    print(parameter)
    print(parameter + '\n')
    error()


def error():
    print(ufo)

s = "fuck"

print_thice(s)

print_thice(s * 3)

print_thice(s + "!" + str(math.pow(2, 55)))
