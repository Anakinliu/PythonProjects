def right_justify2(s):
    ls = ''
    for i in range(70 + len(s)):
        if i <= 69:
            print(i)
            ls += ' '
        else:
            print(i)
            ls += s[i - 70]
    print(ls)

right_justify2('month')
