from PIL import Image
from skimage import morphology
import numpy as np
import cv2 as cv
import scipy.ndimage as pyimg


ori = Image.open('fire.png', mode='r')

ori_np = np.array(ori)

R = ori_np[:, :, 0] > 200
skel = morphology.skeletonize(R)

skel_full = np.array(Image.fromarray(skel).convert('RGB'))

I = skel_full
BW = I[:, :, 0] > 127
G_channel = pyimg.distance_transform_edt(BW)
G_channel[G_channel > 32] = 32
B_channel = pyimg.distance_transform_edt(1 - BW)
B_channel[B_channel > 200] = 200
I[:, :, 1] = G_channel.astype('uint8')
I[:, :, 2] = B_channel.astype('uint8')
Image.fromarray(I).show()

