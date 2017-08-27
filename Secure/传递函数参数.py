def func_1():  # 没有返回值
    print("I 'm func_1")


def func_2(afunction):
    print("In func_2:start:")
    print(type(afunction))
    print(func_2.__class__)
    print(afunction.__class__)

    if afunction.__class__ == func_2.__class__:
        afunction()
    else:
        print("sorry, argument is not a function! It's %s", afunction.__class__)
    print("In func)2:stop.")


# func_2(5)
# func_2(type)


def a_new_decorator(a_func):
    def wraptheFunction():
        print("I am do before exec a_func()")

        a_func()

        print("I am do after exec a_func()")

    return wraptheFunction


def a_func_requiring_decoration():
    print("I need some decoration")


a_func_requiring_decoration()

# a_func_requiring_decoration wrapped
#  by raptheFunction


a_func_requiring_decoration = \
    a_new_decorator(
        a_func_requiring_decoration)

a_func_requiring_decoration()

