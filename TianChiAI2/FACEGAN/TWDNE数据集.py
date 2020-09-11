from torch.utils.data import Dataset
from PIL import Image
import os
import numpy as np
from os import walk

class TWDNE(Dataset):

    def __init__(self, transform):
        """
        :param path: LFW数据集所在的目录
        """
        self.transform = transform
        self.path = 'datasets/TWDNE/data'
        self.images_number = 20000
        self.images_pre = 'datasets/TWDNE/data/example-'
        self.image_type = '.jpg'
        # 统计图片数量
        # 数量太多了，改小点
        # for (_, _, filenames) in walk(self.path):
        #     for file in filenames:  # 遍历 data 文件夹
        #         if file.endswith(self.image_type):  # 过滤文件类型
        #             # print(file)
        #             self.images_number += 1
        #     pass

    def __len__(self):
        return self.images_number

    def __getitem__(self, idx):
        image = Image.open(f'{self.images_pre}{idx}{self.image_type}')
        image.load()
        image = self.transform(image)
        return image



#
# images_filenames = []
# for (dirpath, dirnames, filenames) in walk('datasets/TWDNE/data'):
#     count = 0
#     for file in filenames:
#         if file.endswith('jpg'):
#             # print(file)
#             # count += 1
#             images_filenames.append(file)
#     print(count)
#     # print(f'dirpath-{dirpath}, dirnames-{dirnames}')  # datasets/TWDNE/data, []