
def solution(s):
    result = []
    len_s = len(s)
    for c in range(0, len_s, 2):
        e = ''
        e = e + s[c]
        if c+1 == len_s:
            e = e + '_'
        else:
            e = e + s[c+1]
        result.append(e)
    return result

# 答案之一
import re


def solution2(s):
    """
    很巧妙，
    若s包含奇数个字符，加上最后的_是偶数个，都可以满足.{2}正则
    若s包含偶数个字符，加上最后的_是奇数个，无法满足.{2}正则
    所以不会包含在返回的list里
    :param s:
    :return: 返回满足正则的字符串组成的list
    """
    return re.findall(".{2}", s + "_")


print(solution2('abcdef'))