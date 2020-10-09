"""
两个字符串，s和t，
t由s随机打乱生成，
而且在一个随机位置加入一个随机字符，
返回多加入的那个随机字符

约束：
0 <= s.length <= 1000
t.length == s.length + 1
s和t仅包含小写英文字符。
Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
Example 3:

Input: s = "a", t = "aa"
Output: "a"
Example 4:

Input: s = "ae", t = "aea"
Output: "a"
"""
from collections import Counter


def do(s, t):
    s_lst = sorted(s)
    t_lst = sorted(t)
    idx = -1
    for i in range(len(s_lst)):
        if t_lst[i] != s_lst[i]:
            idx = i
            break
    return t_lst[idx]


def use_Counter(s, t):
    # 字典dict转为list产生结果只有dict的键了
    return list(Counter(t) - Counter(s))[0]


s = 'ae'
t = 'aea'
print(do(s, t))
print(use_Counter(s, t))

