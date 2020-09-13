"""
返回大海捞针中第一次出现的针的索引，如果needle不是大海捞针的一部分，则返回-1。

输入只包含小写英文字符

Input: haystack = "hello", needle = "ll"
Output: 2

Input: haystack = "aaaaa", needle = "bba"
Output: -1

当needle为空弦时我们应该返回什么？
在面试中这是一个很好的问题。
针对此问题，当needle为空字符串时，我们将返回 0。
这与C的strstr（）和Java的indexOf（）一致。
"""
def strStr(haystack, needle):
    if needle:
        try:
            return haystack.index(needle)
            pass
        except ValueError:
            return -1
    return 0

def strStr_newbie(haystack, needle):
    if needle == "":
        return 0
    for i in range(len(haystack)-len(needle)+1):
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                break
            if j == len(needle)-1:
                return i
    return -1
