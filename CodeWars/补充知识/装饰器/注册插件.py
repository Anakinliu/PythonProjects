"""
装饰者不必将他们正在装饰的功能包装起来。
它们还可以简单地注册一个函数的存在，
并将其打开返回。
例如，这可以用来创建一个轻量级的插件架构:

这个简单的插件架构的主要好处是你不需要维护一个插件存在的列表。
这个列表是在插件注册时创建的。
这使得添加一个新插件变得非常简单: 只需定义函数并用@register 对其进行修饰。
"""

import random
PLUGINS = dict()


def register(func):
    """ 注册一个函数作为插件
    没有使用 wrapper
    """
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f'Yo {name}, together we are same'

def regist_test(name):
    greeter_func_name, greeter_func = random.choice(list(PLUGINS.items()))
    print(f'using {greeter_func_name}')
    return greeter_func(name)

print(globals())
