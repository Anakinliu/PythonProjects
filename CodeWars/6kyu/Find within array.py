import inspect

true_if_even = lambda value, index: value % 2 == 0
true_if_odd = lambda v, i: v & 1


def find_in_array(seq, func):
    result = -1
    print(inspect.getsource(func))
    for index, value in enumerate(seq):
        if func(value, index) == True:
            result = index
            break
    return result
    pass


# find_in_array([1,3,5,6,7], true_if_even) # --> 3
print(find_in_array([1, 3, 5, 6, 7], true_if_odd))
print(1 is True)
