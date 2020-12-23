import numpy as np
from PIL import Image
import scipy.ndimage as pyimg

I = np.array(
    Image.open('bamboo.jpg')
)
# RGB
BW = I[:, :, 0] < 250
for i in range(-50, 0):
    print(BW[i])
R_channel = np.ones(BW.shape)
R_channel[I[:, :, 0] < 250] = 255
R_channel[I[:, :, 0] > 250] = 0

# True距离False的距离，False位置为0
G_channel = pyimg.distance_transform_edt(BW)
for i in range(-50, 0):
    print(G_channel[i])
G_channel[G_channel > 32] = 32
B_channel = pyimg.distance_transform_edt(1 - BW)
B_channel[B_channel > 200] = 200
I[:, :, 0] = R_channel
I[:, :, 1] = G_channel.astype('uint8')
I[:, :, 2] = B_channel.astype('uint8')

Image.fromarray(I).show()