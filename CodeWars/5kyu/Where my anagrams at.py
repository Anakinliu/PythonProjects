"""
如果两个单词都包含相同的字母，则它们是彼此的字谜。
例如：
abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

找出一个列表中相同的字谜，您将获得两个输入，一个单词和一个带有单词的数组。
您应该返回所有字谜的数组，如果没有，则返回一个空数组。

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

"""
def anagrams2(word, words):
    #your code here
    sorted_w = sorted(word)
    return [e for e in words if sorted_w == sorted(e)]


# print(anagrams('laser', ['lazing', 'lazy',  'lacer']))
# print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

# Unnamed, e1885, maracil, Ethaw, Cxwto20
from collections import Counter
word = 'aabb'
# print(Counter(word))
def anagrams(word, words):
    w = Counter(word)
    return [e for e in words if Counter(e) == w]


# print(anagrams('laser', ['lazing', 'lazy',  'lacer']))
# print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))