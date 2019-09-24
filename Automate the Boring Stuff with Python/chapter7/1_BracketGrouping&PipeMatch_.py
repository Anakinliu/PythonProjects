mes = '123-456-6666 sd sd 123-123-6666'

# 使用正则
import re
# complie 返回一个Regex对象,记得使用r
phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# 要匹配的整个字符串，开始位置，结束位置
match = phoneRegex.match(mes)  # 返回Match对象
print('use re ', match.group())  # group返回实际匹配文本的字符串
# 使用分组的正则
phoneRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
match = phoneRegex.match(mes)  # 返回Match对象
print('group 1', match.group(1))  # 获取第一组
print('group 1', match.group(2))  # 获取第二组
# 获取所有分组
print(match.groups())
g1, gs = match.groups()

# 使用管道，匹配多个表达式中的一个,第一次出现的将返回
print('管道')
mes = 'Tom is playing Jerry now.'
phoneRegex = re.compile(r'Tom|Jerry')
match = phoneRegex.search(mes)
print(match.group())  # Tom
mes = 'Jerry is playing Tom now.'
phoneRegex = re.compile(r'Tom|Jerry')
search = phoneRegex.search(mes)
print(match.group())

# 管道可以搭配括号执行分组匹配
print('管道可以搭配括号')
mes = 'ABC ABD ABF ABG'
regex = re.compile(r'AB(C|D|E|F)')
res = regex.search(mes, pos=3)  # 遇到第一个匹配结果就返回
print(res.group())