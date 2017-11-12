# coding = UTF-8
x = [1, 2]
y = {
    'z': "i'm z",
    'x': x
}
x.append(y)
# 运行时错误: 超过最大栈深度


def show(the_dict):
    print (the_dict['x'])
    show(the_dict['x'][2])


show(y)

