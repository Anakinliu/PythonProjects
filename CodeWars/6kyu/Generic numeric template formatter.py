"""
Your goal is to create a function to format a number given a template; if the number is not present, use the digits 1234567890 to fill in the spaces.

A few rules:

the template might consist of other numbers, special characters or the like: you need to replace only alphabetical characters (both lower- and uppercase);
if the given or default string representing the number is shorter than the template, just repeat it to fill all the spaces.
A few examples:

numeric_formatter("xxx xxxxx xx","5465253289") == "546 52532 89"
numeric_formatter("xxx xxxxx xx") == "123 45678 90"
numeric_formatter("+555 aaaa bbbb", "18031978") == "+555 1803 1978"
numeric_formatter("+555 aaaa bbbb") == "+555 1234 5678"
numeric_formatter("xxxx yyyy zzzz") == "1234 5678 9012"
"""
# 提交的解法
def numeric_formatter(*template):
    j = len(template)
    if j > 2:
        return -1
    result = []
    str_temp = template[0]
    if j == 2:
        given = template[1]
        count = len(given)
    else:
        given = 10
        count = 1
    for c in str_temp:
        if c.isalpha():
            if j == 2:
                result.append(given[-count])
                count = count - 1
                if count == 0:
                    count = len(given)
                pass
            else:
                result.append(str(count % given))
                count = count + 1
                if count == given + 1:
                    count = 1
                pass
            pass
        else:
            result.append(c)
            pass
    return "".join(result)

print(numeric_formatter("xxx xxxxx xx", '741'))

# 下面是其他用户解法
from itertools import cycle

def numeric_formatter(template, data='1234567890'):
    data = cycle(data)
    #  This function takes an iterable inputs
    #  as an argument and returns an
    #  infinite iterator over the values in inputs
    #  that returns to the beginning once the end of inputs is reached
    return ''.join(next(data) if c.isalpha() else c for c in template)

# 改进我的, 使用默认值参数代替沙雕判断
def numeric_formatter_g(template, given='1234567890'):
    result = []
    str_temp = template
    count = len(given)
    for c in str_temp:
        if c.isalpha():
            result.append(given[-count])
            count = count - 1
            if count == 0:
                count = len(given)
            pass
        else:
            result.append(c)
            pass
    return "".join(result)

