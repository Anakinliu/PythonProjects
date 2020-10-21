from PIL import Image
import numpy as np
import os

def load_image(path, shape=None, crop='center'):
    img = Image.open(path).convert('RGB')

    if isinstance(shape, (list, tuple)):
        # 裁剪以获得形状相同的长宽比(aspect ratio)
        width, height = img.size
        target_width, target_height = shape[0], shape[1]

        aspect_ratio = width / float(height)
        target_aspect = target_width / float(target_height)

        if aspect_ratio > target_aspect:
            # 如果宽度比想要的大，裁剪宽度,保持与target的长宽比一致
            new_width = int(height * target_aspect)
            if crop == 'right':
                img = img.crop((width - new_width, 0, width, height))
            elif crop == 'left':
                img = img.crop((0, 0, new_width, height))
            else:
                img = img.crop(((width - new_width) / 2, 0, (width + new_width) / 2, height))
        else:
            # 裁剪高度
            new_height = int(width / target_aspect)
            if crop == 'top':
                img = img.crop((0, 0, width, new_height))
            elif crop == 'bottom':
                img = img.crop((0, height - new_height, width, height))
            else:
                img = img.crop((0, (height - new_height) / 2, width, (height + new_height) / 2))

        # 长宽比调好了，现在调整大小与target一致
        img = img.resize((target_width, target_height))
    elif isinstance(shape, (int, float)):
        width, height = img.size
        large = max(width, height)
        radio = shape / float(large)
        width_n, height_n = radio * width, radio * height
        img = img.resize((int(width_n), int(height_n)))
    return img


def save_image(path, image):
    res = Image.fromarray(np.uint8(np.clip(image, 0.0, 255.0)))
    res.save(path)


def mkdir_if_not_exists(*args):
    for arg in args:
        if not os.path.exists(arg):
            os.makedirs(arg)
            


