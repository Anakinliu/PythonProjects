#!/usr/bin/env python
# coding: utf-8

import numpy as np


x_data = [338, 333, 328, 207, 226, 25, 179, 60, 208, 606]
y_data = [640, 633, 619, 393, 428, 27, 193, 66, 226, 1591]

w_ = np.random.rand(10) * 10

b_ = np.random.rand(10) * 20
# b_ = b_ * 100


x_data = np.array(x_data, dtype=float)
y_data = np.array(y_data, dtype=float)


# L_ = np.sum(np.square(y_data - (b_ + w_ * x_data)))

# print('L_', L_)
# print()

learning_rate = 0.00000001

# dw = 2 * (y_data - (b_ + w_ * x_data)) * (-x_data)
#
# db = 2 * (y_data - (b_ + w_ * x_data)) * (-1)

# print(dw)
# print(db)

for i in range(1000000):
    w_ = w_ - learning_rate * 2 * (y_data - (b_ + w_ * x_data)) * (-x_data)
    b_ = b_ - learning_rate * 2 * (y_data - (b_ + w_ * x_data)) * (-1)

print(w_)
print(b_)
L_ = np.square(y_data - (b_ + w_ * x_data))
print('f star: ', np.min(L_))

index = np.argmin(L_)
print('w star: ', w_[index])
print('b star: ', b_[index])

