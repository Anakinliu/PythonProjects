"""
在此kata中，您必须创建输入字符串的所有排列并删除重复项（如果存在）。
这意味着，您必须按所有可能的顺序对输入中的所有字母进行混洗。
Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
ABCD -> ABCD, ACBD, BACD, BCAD, CBAD, CABD,
AB -> AB, BA
"""


def permutations(string):
    # def do(chosen, remaining, res):
    #     if len(remaining) == 1:
    #         res.append(''.join(remaining+chosen))
    #         return
    #     d = remaining.pop()
    #     chosen.append(d)
    #     do(chosen, remaining, res)
    #     chosen.pop()
    #     remaining.insert(0, d)
    #     do(chosen, remaining, res)

    def do(s, fixed_len, res):
        if fixed_len == len(s) - 1:
            res.add(''.join(s))
            return
        do(s, fixed_len + 1, res)
        for i in range(fixed_len + 1, len(s)):
            temp = s.copy()
            temp[fixed_len], temp[i] = temp[i], temp[fixed_len]
            do(temp, fixed_len + 1, res)

    r = set()
    # do(c, remain, r)
    do(list(string), 0, r)
    print(list(r))
    pass


# Sebek, maxx_d2
def permutations2(string):
    if len(string) == 1:
        return set(string)
    first = string[0]
    rest = permutations2(string[1:])
    result = set()
    for i in range(0, len(string)):
        for p in rest:
            result.add(p[0:i] + first + p[i:])
    return result


print(permutations2('ABC'))
