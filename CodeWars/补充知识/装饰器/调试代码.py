import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        # !r意思是repr() is used to represent the value
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

@debug
def f(w, m='m'):
    print(f'{w} say 233, {m}')

# f('wa')
import math
# 调试标准库里的函数
my_fac = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / my_fac(n) for n in range(terms))

approximate_e()