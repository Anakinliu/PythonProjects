"""
https://www.codewars.com/kata/5ebcfe1b8904f400208e3f0d/train/python
允许 重用函数名， 调用返回所有重名的结果

实现两件事：
1. 一种删除特定函数的方法
2. 一种删除所有已存储的函数的方法。
delete方法必须按如下方式工作：
@FuncAdd
def foo():
    return 'Hello'

clear() 方法：
@FuncAdd
def foo():
    return 'Hello'

FuncAdd.clear() # Delete all decorated functions
foo() # Should raise NameError
"""

import functools
FUNC_DICT = dict()
class FuncAdd:
    # Good Luck!
    def __init__(self, func):
        functools.update_wrapper(self, func)
        # self.func = func
        self.func_name = func.__name__
        if self.func_name not in FUNC_DICT.keys():
            FUNC_DICT[self.func_name] = list()
        FUNC_DICT[self.func_name].append(func)

    # 当调用被装饰的方法时，实际上是调用的这个 __call__ 方法
    def __call__(self, *args, **kwargs):
        if self.func_name not in FUNC_DICT.keys():
            raise NameError
        return tuple([e(*args, **kwargs) for e in FUNC_DICT[self.func_name]])

    @staticmethod
    def delete(func):
        FUNC_DICT.pop(func.__name__)
        pass

    @staticmethod
    def clear():
        FUNC_DICT.clear()
        pass


@FuncAdd
def foo():
    return 'hello'


@FuncAdd
def foo():
    return 'world'

# print(foo())


@FuncAdd
def bar(n):
    return n + 2


@FuncAdd
def bar(n):
    return n * 2


# print(bar(n=5))


@FuncAdd
def spam():
    return 'Hello'

@FuncAdd
def spam():
    return 'World'

@FuncAdd
def ham():
    return 'Eggs'


FuncAdd.delete(spam)
spam()