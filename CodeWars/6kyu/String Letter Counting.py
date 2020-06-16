def string_letter_count(s):
    s = s.lower()
    res_dict = dict()
    i = 0
    for c in s:
        if 'a' <= c <= 'z':
            if c not in res_dict.keys():
                res_dict.setdefault(c, 1)
            else:
                res_dict[c] += 1
    items = sorted(res_dict.items())
    # print(items)
    res_str = ""
    for c, n in items:
        res_str = res_str + str(n) + c
    # print(res_str)
    return res_str

# string_letter_count("This is a test sentence.")
# string_letter_count("")
# string_letter_count("555")

# =======大神解法

def string_letter_count(s):
    s = s.lower()
    m = ''
    for i in sorted(list(set(s))):  # 去重，排序，迭代
        if i.islower():  # lower可以把空格与标点过滤掉
            m += str(s.count(i)) + i  # str.count可以啊
    return m