"""
加密字符串，加密规则为使用原文字符的后面的第13个字符，特殊字符与数字不加密

test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")
"""


def rot13(message):
    res = []
    for i in message:
        if 65 <= ord(i) <= 90:
            res.append(chr((ord(i) + 13 - 65) % 26 + 65))
        elif 97 <= ord(i) <= 122:
            res.append(chr((ord(i) + 13 - 97) % 26 + 97))
        else:
            res.append(i)
    # print(res)
    return ''.join(res)


# rot13("test")#"grfg"
# rot13("Test")#"Grfg"
# print(ord('A'))
# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))

# warwickwang的解答
from string import ascii_lowercase as lc, ascii_uppercase as uc
def rot13(message):
    # 制作一个翻译器
    tran = message.maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13])
    # 使用翻译器
    return message.translate(tran)

print(rot13("test"))#"grfg"
print(rot13("Test"))#"Grfg"