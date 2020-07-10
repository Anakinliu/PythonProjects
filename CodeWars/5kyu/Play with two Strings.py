def f(a, b):
    dct = dict()
    case_b = b.lower()
    a_set = set(a)
    for char in a_set:
        if char not in dct.keys():
            dct[char] = 0
        char_count = case_b.count(char.lower())
        dct[char] += char_count
    result = []
    print(dct)
    for char in a:
        if dct[char] % 2 == 1:
            if char.isupper():
                result.append(char.lower())
            else:
                result.append(char.upper())
        else:
            result.append(char)
    return "".join(result)

a = "abcdeFgtrzw"
b = "defgGgfhjkwqe"
# "abcDeFGtrzW
# DEFGgGFhjkWqE"
# f('abab', 'bababa')
print(f(a,b))

# 列表生成式 jessi_jr13, ItsTheLAW
def work_on_strings(a, b):
    new_a = [letter if b.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in a]
    new_b = [letter if a.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in b]
    return ''.join(new_a) + ''.join(new_b)

