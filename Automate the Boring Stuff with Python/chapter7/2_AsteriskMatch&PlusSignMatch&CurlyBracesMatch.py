import re
# 使用问号，表明这段文本在不在都会匹配，0次或1次
mes = 'it is ours country'
regex = re.compile(r'our(s) country?')
res = regex.search(mes)
print(res.group())

# 星号，零次及以上任意次
print('星号')
msg = 'ooops ooooooops, you lost phone'
regex = re.compile(r'(o)*ps')
res = regex.match(msg)
print(res.group())

# 使用加号匹配一次或多次
print('加号')
msg = 'batman batwoman batwowoman'
regex = re.compile(r'bat(wo)+man')
res = regex.search(msg)
print(res.group())


# 花括号匹配指定次数（范围）
print('花括号')
msg = 'ooops oooops , how '
regex = re.compile(r'(o){3,5}ps')
res = regex.match(msg)
print(res.group())
