i = 11
"""
因为要想等，二进制首位不能是 0， 则末位也不能是 0，故只能是奇数
"""
while True:
    # replace考虑反转后的前缀
    if str(bin(i))[::-1].replace('b0', '') == str(bin(i)).replace('0b', '') \
            and str(oct(i))[::-1].replace('o0', '') == str(oct(i)).replace('0o', '') \
            and str(i)[::-1] == str(i):
        print(i)
        break
        pass
    i += 2

