import turtle

# 创建一个Turtle对象并赋给bob变量

bob = turtle.Turtle()

# bob已经得到了在turtle中定义的Turtle类型的一个对象!

print(bob)

# 向前移动100像素(pixel)

for i in range(72):     # 循环没有完成时结束程序会报错!
    bob.fd(100)
    bob.lt(5)

"""
bk 前进或后退
lt 左转, 单位是度
rt 右转
"""

# 让窗口等待用户操作

turtle.mainloop()

