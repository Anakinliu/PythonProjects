roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    length = len(roman)
    if length < 1:
        return 0
    # 列表模拟栈
    stack = []
    top_index = -1
    decimal = 0
    for e in range(length):
        e_dec = roman_dict[roman[e]]

        stack.append(e_dec)
        top_index = top_index + 1

        print(stack)
        if e_dec < stack[top_index] and \
                e + 1 < length and \
                roman_dict[roman[e]] :

        # if len(stack) == 2:
        #     if stack[1] >= stack[0]:
        #         decimal = decimal + (stack[0] + stack[1])
        #         pass
        #     elif stack[1] < stack[0]:
        #         decimal = decimal + (stack[0] - stack[1])
        #     stack.clear()
    return decimal


print(solution('MMVIII'))