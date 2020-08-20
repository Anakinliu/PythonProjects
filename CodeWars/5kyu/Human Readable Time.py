"""
输入一个整数秒数，输出HH:MM:SS

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59

最大时间不超过359999 (99:59:59)
"""
def make_readable(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    # print(f'{h:02}:{m:02}:{s:02}')
    return f'{h:02}:{m:02}:{s:02}'


# print(make_readable(99))
print(divmod(8, -3))