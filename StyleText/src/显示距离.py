from PIL import Image
import numpy as np
import scipy.ndimage as pyimg

img_path = '../data/oth/A.png'
I = np.array(Image.open(img_path))



def text_image_preprocessing(filename):
    I = np.array(Image.open(filename))
    BW = I[:, :, 0] > 127
    G_channel = pyimg.distance_transform_edt(BW)
    G_channel[G_channel > 32] = 32
    B_channel = pyimg.distance_transform_edt(1 - BW)
    B_channel[B_channel > 200] = 200
    I[:, :, 1] = G_channel.astype('uint8')
    I[:, :, 2] = B_channel.astype('uint8')
    return Image.fromarray(I)