import functools


class CountCalls:
    def __init__(self, func):
        # 您需要使用 functools.update_wrapper ()函数，而不是@functools.wraps(func)
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_whee():
    print("Whee!")

say_whee()  # 其实调用的是 __call__ 方法
print(say_whee.__name__)

lst = [1,3,5,3]
print(tuple(lst))
x = {e for e in lst}
print(x)
print(type(x))
print(x)