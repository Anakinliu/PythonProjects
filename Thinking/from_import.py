# coding=utf-8
from __future__ import division  # 导入division模块的__future__子模块


def divide(numerator, denominator, detect_repetition=True, digit_limit=None):
    # 如果是无限小数，必须输入限制的返回小数位数:digit_limit
    # digit_limit = 5，表示小数位数5位，注意这里的小数位数是截取，不是四舍五入.
    if not detect_repetition and digit_limit == None:
        return None

    decimal_found = False

    v = numerator // denominator
    numerator = 10 * (numerator - v * denominator)
    answer = str(v)

    if numerator == 0:
        return answer

    answer += '.'

    # Maintain a list of all the intermediate numerators
    # and the length of the output at the point where that
    # numerator was encountered. If you encounter the same
    # numerator again, then the decimal repeats itself from
    # the last index that numerator was encountered at.
    states = {}

    while numerator > 0 and (digit_limit == None or digit_limit > 0):

        if detect_repetition:
            prev_state = states.get(numerator, None)
            if prev_state != None:
                start_repeat_index = prev_state
                non_repeating = answer[:start_repeat_index]
                repeating = answer[start_repeat_index:]
                return non_repeating + '[' + repeating + ']'
            states[numerator] = len(answer)

        v = numerator // denominator
        answer += str(v)
        numerator -= v * denominator
        numerator *= 10
        if digit_limit != None:
            digit_limit -= 1

    if numerator > 0:
        return answer + '...'
    return answer


# 将除法变得和python3一样
print type(divide(5, 3))

print 'ee' * 5

print `22` + '22'
# 上句的``等同于下句的repr()
print repr(22) + '22'
# 然而实际编码中绝大部分是使用str()而非repr()或者``
# repr()可用于无法打印的字符

# 测试格式化输出, 多个需要加括号, 优雅
print 'i am %d years old %s' % (20, '!!!')

# 一个字符串就是一个数组
print 'abcdef'[0]
print 'abcdef'[-1]

# 截取, 不包括-2
print 'abcdef'[0:-2]

# python有去空格函数
print '   sdsd   '.strip()
