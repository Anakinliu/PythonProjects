"""
给定 字符串 数字 序列，返回丢失的数字，如果没有丢失的，返回 -1

**序列总是升序的**

For example:

missing("123567") = 4
missing("899091939495") = 92
missing("9899101102") = 100
missing("599600601602") = -1 -- no number missing
missing("8990919395") = -1 -- error in sequence. Both 92 and 94 missing.

Test.it("Basic tests")
Test.assert_equals(missing("123567"),4)
Test.assert_equals(missing("899091939495"),92)
Test.assert_equals(missing("9899101102"),100)
Test.assert_equals(missing("599600601602"),-1)
Test.assert_equals(missing("8990919395"),-1)
Test.assert_equals(missing("998999100010011003"),1002)
Test.assert_equals(missing("99991000110002"),10000)
Test.assert_equals(missing("979899100101102"),-1)
Test.assert_equals(missing("900001900002900004900005900006"),900003)
"""
# 1. 怎么识别是哪个数列？
def vs(test, init_d, s):
    # test : int 元素的数组
    # s : 题目给的一个字符串
    count = 0
    # print(test, init_d, s)
    # s 的最后一个数字对应的test中的元素的下标
    max_idx = 0
    for idx, e in enumerate(test):
        if str(e) in s[count:]:
            count += len(str(e))
            max_idx = idx
    # print(f'test {test}; max_idx {max_idx}; count {count}')
    return count, max_idx


def missing(s):
    # 初始时，假设一位的数字就是序列的第一个值
    # init_d = 1
    len_original = len(s)
    possible_len = 1
    final_test = []
    final_idx = 0
    for init_d in range(1, len_original // 2 + 1):
        e = int(s[:init_d])
        test = [e]
        # 考虑到 s 本身少了一个值
        while len(test) <= len_original + 1:
            e += 1
            test.append(e)
        # 比较 test 与 original，求最大匹配个数，赋值给 res
        count, max_idx = vs(test, init_d, s)
        # print(count, max_idx, init_d)
        if count > possible_len:
            possible_len = count
            final_test = test
            final_idx = max_idx

    final_test = final_test[:final_idx+1]
    # print(final_test)
    step = 0
    flag = 0
    result = -1
    for e in final_test:
        if str(e) not in s[step:]:
            flag += 1
            if flag > 1:
                return -1
            result = e
        else:
            step += len(str(e))

    return result

    # b 要重新考虑进位的情况
    # b =
    # print(a, b)
    # for e, f in zip(a, b):
    #     if e != f:
    #         print(e)
    #         return e
    # print(-1)
    # return -1

# detect("123567")  # 4
# detect("899091939495")  # 92
# print(detect("89908992"))  # 92
# 89908992 -> 8991 or 91?

# missing("8990919395")  # -1
# missing("998999100010011003")  # 1002
# missing("99991000110002")  # 10000

print(missing("123567"))  # 4
print(missing("899091939495"))  # 92
print(missing("9899101102"))  # 100
print(missing("599600601602"))  # -1
print(missing("8990919395"))  # -1
print(missing("998999100010011003"))  # 1002
print(missing("99991000110002"))  # 10000
print(missing("979899100101102"))  # -1
print(missing("900001900002900004900005900006"))  # 900003

