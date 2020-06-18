def hex_string_to_RGB(hex_string):
    d = dict()
    d['r'] = int(hex_string[1:3], base=16)
    d['g'] = int(hex_string[3:5], base=16)
    d['b'] = int(hex_string[5:7], base=16)
    print(d)
    # your code here
    return d


hex_string_to_RGB("#FF9933")


def solution(s):
    return {i: int(s[j:j + 2], 16) for i, j in zip('rgb', [1, 3, 5])}
