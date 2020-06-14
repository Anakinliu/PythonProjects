"""
 @Description      给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
 请根据这个假设，如果反转后整数溢出那么就返回 0。
 @author          linux
 @create          2020-05-09 8:59
"""


def reverse(x: int) -> int:
    strx = str(abs(x))
    listx = list(strx)
    listx.reverse()
    res = int("".join(listx))
    if x >= 0:
        if res > 2**31 - 1:
            return 0
        else:
            return res
    else:
        if -res < -(2**31):
            return 0
        else:
            return -res
    pass

# print(int('-0021'))
print(-8463847412 < -(2**31))
print(reverse(-2147483648))