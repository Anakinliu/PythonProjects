# https://www.codewars.com/kata/5a959662373c2e761d000183/python
#       10 display width, 4 step
#ticker('Hello world!', 10, 4)   # '      Hell'

# test.assert_equals(ticker('Beautiful is better than ugly.', 10, 30), 'than ugly.')
# text = 'Beautiful is better than ugly.'
text = 'Foobar'
# print(len(text))
def ticker(text, width, tick):
    text_len = len(text)
    if width + text_len < tick:
        tick = tick % (width + text_len)
    print(tick)
    if width > tick:
        space = '0' * (width - tick)
        left = space + text[:tick]
        left_len = len(left)
        right = '0' * (width - left_len)
        return left + right
    else:
        left = text[tick - width:tick]
        left_len = len(left)
        if left_len < width:
            right =  '0' * (width - left_len)
            return left + right
        return left

# codewar user : eLCiao
def ticker2(text, width, tick):
    tick %= len(text) + width
    text = ' ' * width + text + ' ' * width
    return text[tick : tick + width]

for tick in range(50):
    print(ticker2(text, 10, tick))