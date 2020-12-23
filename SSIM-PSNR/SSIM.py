import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim
from numpy import linalg as LA

style_path = 'data/fire.png'
target1_path = 'data/10000.png'
target2_path = 'data/fire_fire-huo_20.png'

style_ndarray = np.asarray(Image.open(style_path).convert('RGB'))
target1_ndarray = np.asarray(Image.open(target1_path).convert('RGB'))
target2_ndarray = np.asarray(Image.open(target2_path).convert('RGB'))


# psnr
def psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr


psnr_const_1 = psnr(target1_ndarray, style_ndarray)
psnr_const_2 = psnr(target2_ndarray, style_ndarray)

# SSIM structural similarity index
ssim_const_1 = ssim(target1_ndarray, style_ndarray, multichannel=True)
ssim_const_2 = ssim(target2_ndarray, style_ndarray, multichannel=True)

print('SSIM:')
print(f'NST: {ssim_const_1}')
print(f'ShapeMatchingGAN: {ssim_const_2}')

print('PSNR:')
print(f'{psnr_const_1}')
print(f'{psnr_const_2}')

