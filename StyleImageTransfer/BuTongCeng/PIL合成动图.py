from PIL import Image
import os
import re
path = 'target/fire+火+random_init+c_w-1e3+conv5_1-02+conv4_1-02+conv3_1-02/'
images = []
file_names = []

with os.scandir(path) as files:
    for file in files:
        file_names.append(file.name)
# print(file_names)

file_names = sorted(file_names, key=lambda x: int(re.search('[0-9]+\\.', x).group()[:-1]))

# print(file_names)
for file_name in file_names:
    images.append(Image.open(path+file_name))

img = Image.new('RGB', images[0].size)

img.save('target/gifs/huo.gif',
               save_all=True, append_images=images[:], optimize=False, duration=200, loop=0)

