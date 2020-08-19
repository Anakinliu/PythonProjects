# 封装函数，加上连哥哥输出
def a(b):
    def b_wrapper():
        print('---start---')
        b()
        print('---end---')
    return b_wrapper

def b():
    print("bb")

new_b = a(b)
new_b()
