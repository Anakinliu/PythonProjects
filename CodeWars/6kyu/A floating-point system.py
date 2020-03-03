# 给定一个正小数，和digitsNumber，将正小数扩展成digitsNumber位
# mantissa * radix ^ exponent
# 例如aNumber = 0.06 =》aNumber : 6000000000 * 10 ^ -11


"""
mantExp(aNumber, digitsNumber)

The function mantExp(aNumber, digitsNumber) will return aNumber in the form of a string: "mantissaPexponent" (concatenation of "mantissa", "P", "exponent"). So:

Examples:
mantExp(0.00618, 10) returns "6180000000P-12".  8个0
mantExp(72.0, 12)   returns "720000000000P-10"  10个0
mantExp(1.0, 5) returns "10000P-4"  4个0
mantExp(123456.0, 4) returns "1234P2"

检查：
1 <= digitsNumber <= 15
0 < aNumber < 5.0 ^ 128

小于1的计算小数点右边第几位非0，
"""
def mantExp3(a_number, digits_number):
    if digits_number < 1 or digits_number > 15:
        return -1
    if a_number <= 0.0 or a_number >= 5.0 ** 128.0:
        return -1

    # print(str(a_number))
    str_a_number = '{:f}'.format(a_number)
    if str_a_number.find('.') is -1:
        return str_a_number[:digits_number] + 'P'

    len_str_number = len(str_a_number)
    # 先看大于等于1的
    index_of_point = str_a_number.index('.')
    print(index_of_point)
    zeros = digits_number - index_of_point
    if a_number >= 1.0:
        if index_of_point >= digits_number:
            return str_a_number[:digits_number] + 'P' + str(index_of_point - digits_number)
        else:
            str_res = str(a_number * (10 ** zeros))
            return str_res[:digits_number] + 'P-' + str(zeros)

    else:
        # 再看大于0， 小于1的
        mul10 = a_number
        no_zero = -1
        while mul10 < 1.0:
            mul10 = mul10 * 10
            no_zero = no_zero + 1
        print(no_zero)
        return str_a_number[no_zero+2:no_zero + digits_number + 2] + '0' * (digits_number + no_zero - (len_str_number - 2)) + 'P-' + str(digits_number + no_zero)

def mant_exp(a_number, digits_number):
    exp = 0
    m = a_number
    num = 10**digits_number
    if m < num: #negative exponent
       while m*10 < num:
            m *= 10
            exp -= 1
    else:
       while m >= num:
            m /= 10
            exp += 1
    return str(int(m)) + 'P' + str(exp)

print(mant_exp(0.00618, 10))

# print(mantExp3(72.0, 12))

# print(mantExp(1.0, 5))
# print(mantExp(123456.0, 4))
# print(mantExp(1.103, 10))  # expect 1103000000P-9

# print(mantExp3(72.234567, 12))  # OK
# print(mantExp3(0.3333333333333333, 15))
# 333333333333333P-15  want
# 333333333333333P-15
# 3333333333333P-15
# 3333333333333333P-15
# 333333333333P-15
# 3333333333333P-15
# 3333333333333333P-15

# 3333333333333333

# print(mantExp3(1.8446744073709552e+19, 15))

# ACTUAL
# 1.8446744073709P-14
# 184467440737095P5  want
# 184467440737095P5


