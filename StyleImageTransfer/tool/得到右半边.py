from PIL import Image
import numpy as np

two82_1 = Image.open('data/82-1.png')
two82_2 = Image.open('data/82-2.png')
two82_3 = Image.open('data/82-3.png')
two82_4 = Image.open('data/82-5.png')
one = Image.open('data/弹.png')
new = Image.new('RGB', (1600, 320))

# print(two.size)  # w,h
# print(tan.size)
# two_array = np.asarray(two)
# tan_array = np.asarray(tan)
# new_array = np.asarray(new)
# print(two_array.shape)
# print(tan_array.shape)
# two_array[:, 320:, :] = two_array[:, :, :]
# new[:, 320:, :] = two_array[:, :, :]
new_pixels = new.load()
two82_1_pixels = two82_1.load()
two82_2_pixels = two82_2.load()
two82_3_pixels = two82_3.load()
two82_4_pixels = two82_4.load()

one_pixels = one.load()
for i in range(new.size[0]):
    for j in range(new.size[1]):
        if i < 320:
            new_pixels[i, j] = one_pixels[i, j]
        if 320 <= i < 640:
            new_pixels[i, j] = two82_1_pixels[i, j]
        if 640 <= i < 960:
            new_pixels[i, j] = two82_2_pixels[i-320, j]
        if 960 <= i < 1280:
            new_pixels[i, j] = two82_3_pixels[i-640, j]
        if 1280 <= i < 1600:
            new_pixels[i, j] = two82_4_pixels[i-960, j]
new.show('here')
new.save('data/82_raw.png', format='png')
