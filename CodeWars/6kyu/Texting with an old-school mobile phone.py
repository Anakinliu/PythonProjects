"""
Texting with an old-school mobile phone
- default case is lowercase.
- space between 2 (or more) such letters (to type hihi, press 44 444 44 444)
- Note that after holding a key you don't need to wait to press another key.
- Note that even though those 2 letters are on the same key, you have to switch case between them, so you don't have to wait.

"""
# 不用考虑非法输入
def send_message(message):
    board = {'1':['.', ',', '?', '!'],
             '2':['a', 'b', 'c'],
             '3':['d', 'e', 'f'],
             '4':['g', 'h', 'i'],
             '5':['j', 'k', 'l'],
             '6':['m', 'n', 'o'],
             '7':['p', 'q', 'r', 's'],
             '8':['t', 'u', 'v'],
             '9':['w', 'x', 'y', 'z'],
             '*':["'", '-', '+', '='],
             '0':[' '],
             '#':[]}
    m_len = len(message)
    result = []
    upper_state = False
    for i, char in enumerate(message):
        # 数字直接长按加上，不用等待，没有大小写区分
        if char.isdigit() or char == '*' or char == '#':
            result.append(char)
            result.append('-')
        # 非数字，注意标点符号类也不区分大小写

        for key, values in board.items():
            for index, alpha in enumerate(values):
                if char.isupper() and upper_state is False:
                    upper_state = True
                    result.append('#')
                if char.islower() and upper_state is True:
                    upper_state = False
                    result.append('#')
                if char.lower() == alpha:
                    result.append(key*(index + 1))
                    if i+1 <= m_len - 1:
                        # 下一个字符是相同大小写的
                        if message[i].islower() == message[i+1].islower() \
                                and message[i+1].lower() in values:
                            result.append(" ")
                        # 下一个字符直接是数字
                        if message[i+1] in key:
                            result.append(" ")

    return "".join(result)
"""
    ["hey", "4433999"],
    ["one two three", "666 6633089666084477733 33"],
    ["Hello World!", "#44#33555 5556660#9#66677755531111"],
    ["Def Con 1!", "#3#33 3330#222#666 6601-1111"],
    ["A-z", "#2**#9999"],
    ["1984", "1-9-8-4-"],
    Big thanks for checking out my kata
"""
print(send_message("Big thanks for checking out my kata"))


# 大神Blind4Basics解法
HOLDERS = '12345678910*#'
TOME = {c: n * str(i) for i, seq in enumerate(' /.,?!/abc/def/ghi/jkl/mno/pqrs/tuv/wxyz'.split('/'))
        for n, c in enumerate(seq, 1)}
TOME.update({c: c + '-' for c in HOLDERS})
TOME.update({c: n * '*' for n, c in enumerate("'-+=", 1)})

print(TOME)
def send_message(s):
    isUp, out = 0, []

    def press(seq):
        if out and out[-1][-1] == seq[0]: seq = ' ' + seq
        out.append(seq)

    for c in s:
        if c.isalpha() and isUp != c.isupper():
            press('#')
            isUp ^= 1
        press(TOME[c.lower()])

    return ''.join(out)
