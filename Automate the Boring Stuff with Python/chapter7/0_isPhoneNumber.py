def isPhoneNumber(text):
    if len(text) < 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
        if text[7] != '-':
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True


# print(isPhoneNumber('123-123-1s234'))
mes = '123-456-6666 sd sd 123-123-6666'
print('use normal ')
for i in range(len(mes)):
    chunk = mes[i:i+12]
    if isPhoneNumber(chunk):
        print('found ', chunk)
        pass
    pass
print('Done')



