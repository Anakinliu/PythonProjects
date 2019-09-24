# Python正则默认是贪心的，
# 有二义时默认匹配最长的字符串

# 花括号的贪心与非贪心实例
import re
msg = 'HaHaHaHaHaHa000'
greedyRegex = re.compile(r'(Ha){3,5}')
res = greedyRegex.search(msg)
print(res.group())  # 5个Ha

# 问号此时的含义：声明进行非贪婪匹配
nongreedyRegex = re.compile(r'(Ha){3,5}?')
res = nongreedyRegex.search(msg)
print(res.group())
