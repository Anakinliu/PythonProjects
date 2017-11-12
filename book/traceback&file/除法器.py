print("=======start=======")
print("=======exit q=======")

while True:
    first_n = input("first number: ")
    # input函数得到的是str类型
    if first_n is 'q':
        break
    second_n = input("second number: ")
    if second_n is 'q':
        break
    try:
        answer = int(first_n) / int(second_n)
    except ZeroDivisionError:
        print("0 can't be division!")
    else:
        print("answer is " + str(answer))