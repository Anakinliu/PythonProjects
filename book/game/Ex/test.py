"""
AUTHOR: Anakinliu
DATE: 17.11.25
TIME: 20:57
DO TOUR BEST
"""
myGlobal = 5


def func1():
    global myGlobal
    print(myGlobal)
    myGlobal = 42


def func2():
    print(myGlobal)


func1()  # 5
func2()  # 42
