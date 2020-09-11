from torch.utils.data import Dataset
from PIL import Image
import os
import numpy as np


class LFW(Dataset):

    def __init__(self, path='datasets/lfw-deepfunneled/', load=False, transform=None):
        """
        :param path: LFW数据集所在的目录
        :param load: False 从新读取数据并保存numpy到文件 True 则直接读取Numpy文件
        """
        self.path = path
        self.transform = transform

        self.images = []
        self.real_labels = []
        self.labels = []
        # 读取数据集所有文件， 13233张
        if load:
            self.images = np.load('saves/images.npy')
            self.labels = np.load('saves/labels.npy')
            self.real_labels = np.load('saves/real_labels.npy')
        else:
            i = 0
            for root, dirs, files in os.walk(self.path):
                has = False  # 去掉 ‘’
                for file in files:
                    has = True
                    # print(root.split('/')[-1], file)
                    a_img = Image.open(root + '/' + file)
                    a_img.load()
                    self.images.append(np.asarray(a_img))
                    self.labels.append(i)
                    pass
                if has:
                    self.real_labels.append(root.split('/')[-1])
                i += 1
                pass
            self.images = np.asarray(self.images)
            self.labels = np.asarray(self.labels)
            self.real_labels = np.asarray(self.real_labels)
            np.save('saves/images.npy', self.images)
            np.save('saves/labels.npy', self.labels)
            np.save('saves/real_labels.npy', self.real_labels)

    def __len__(self):
        # print(total)
        return len(self.images)

    def __getitem__(self, idx):
        # print(self.data[idx])
        # print(self.data[idx].shape)
        img = self.images[idx]
        if self.transform is not None:
            img = self.transform(Image.fromarray(img))
        return img, self.labels[idx]

