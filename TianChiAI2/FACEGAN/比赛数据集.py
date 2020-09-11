from torch.utils.data import Dataset
from PIL import Image
import os
import numpy as np
import pandas as pd


class LittleLFW(Dataset):

    def __init__(self, data_path='datasets/images/', csv_path='datasets/securityAI_round1_dev.csv',
                 load=False, transform=None):
        """
        :param data_path:
        :param csv_path:
        :param load: False 从新读取数据并保存numpy到文件 ; True 则直接读取Numpy文件
        :param transform: 就 torchvision.transforms 的transforms
        """
        self.data_path = data_path
        self.csv_path = csv_path
        self.transform = transform
        self.images = []
        self.labels = []
        self.real_labels = []
        if load:
            self.images = np.load('saves/LittleLFW/images.npy')
            self.labels = np.load('saves/LittleLFW/labels.npy')
            self.real_labels = np.load('saves/LittleLFW/real_labels.npy')
            pass
        else:
            csv_content = pd.read_csv(csv_path)
            # 712 个图片，来自不同的人
            for file_name, label, name in zip(csv_content['ImageName'],
                                              csv_content['ImageId'],
                                              csv_content['PersonName']):
                a_img = Image.open(data_path + file_name)
                a_img.load()
                self.images.append(np.asarray(a_img))
                self.labels.append(int(label))
                self.real_labels.append(name)
            self.images = np.asarray(self.images)
            self.labels = np.asarray(self.labels)
            os.makedirs('saves/LittleLFW', exist_ok=True)
            np.save('saves/LittleLFW/images.npy', self.images)
            np.save('saves/LittleLFW/labels.npy', self.labels)
            np.save('saves/LittleLFW/real_labels.npy', self.real_labels)
            pass

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
#
# llfw = LittleLFW(load=False)
# print(llfw[0])
