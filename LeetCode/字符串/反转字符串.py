"""
 @Description      
 @author          linux
 @create          2020-05-09 8:37
"""
"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
"""
# s : List[str]
def reverseString(s):
    len_s = len(s)
    if len_s <= 1:
        return s
    for i in range(0, len_s // 2):
        temp = s[i]
        s[i] = s[len_s - i - 1]
        s[len_s - i - 1] = temp
    print(s)

# 调用
def reverseString(s):
    s.reverse()  # 原地反转

reverseString(["H","a","n","n","a","h"])
reverseString(["h","e","l","l","o"])
