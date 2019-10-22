import threading
import time

def task(n):
    while n > 0:
        n -= 1

# s_time = time.time()
# task(100000000)
# e_time = time.time()
# print(e_time - s_time)  # 6.034 second

#-----两个线程---------

s_time = time.time()

thred1 = threading.Thread(target=task, args=[50000000])
thred2 = threading.Thread(target=task, args=[50000000])

thred1.start()
thred2.start()

# join阻塞主线程
thred1.join()
thred2.join()

e_time = time.time()

print(e_time - s_time)  # 5.814 second
"""
GIL: 全局解释器锁（英语：Global Interpreter Lock，缩写GIL），是计算机程序设计语言解释器用于同步线程的一种机制，它使得任何时刻仅有一个线程在执行。[1]即便在多核心处理器上，使用 GIL 的解释器也只允许同一时间执行一个线程。

作者：聪明叉
链接：https://juejin.im/post/5c13245ee51d455fa5451f33
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
