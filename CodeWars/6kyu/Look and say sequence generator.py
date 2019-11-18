"""
The look and say sequence is a sequence in which each number is the result of a "look and say" operation on the previous element.

Considering for example the classical version startin with "1": ["1", "11", "21, "1211", "111221", ...]. You can see that the second element describes the first as "1(times number)1", the third is "2(times number)1" describing the second, the fourth is "1(times number)2(and)1(times number)1" and so on.

Your goal is to create a function which takes a starting string (not necessarily the classical "1", much less a single character start) and return the nth element of the series.
look_and_say_sequence("1", 1)   == "1"
look_and_say_sequence("1", 3)   == "21"
look_and_say_sequence("1", 5)   == "111221"
look_and_say_sequence("22", 10) == "22"
look_and_say_sequence("14", 2)  == "1114"

2222334 -> 422314 -> 1422131114
"""
def look(first_element):
    left = 0
    right = left + 1
    end = len(first_element)
    count = 1
    result = []
    while right < end:
        if first_element[right] == first_element[left]:
            count = count + 1
            right = right + 1

        else:
            result.append(str(count))
            result.append(str(first_element[left]))
            left = right
            right = left + 1
            count = 1

    if right >= end:
        result.append(str(count))
        result.append(str(first_element[left]))
    return "".join(result)


def look_and_say_sequence(first_element, n):
    if n == 1:
        return first_element
    return look_and_say_sequence(look(first_element), n - 1)



# print(look("1"))
print(look_and_say_sequence("1", 3))

from itertools import groupby
from functools import reduce
def look_and_say_sequence_2(first_element, n):
    # Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.
    return reduce(lambda s, _: ''.join('%d%s' % (len(list(g)), n) for n, g in groupby(s)), range(n - 1), first_element)
