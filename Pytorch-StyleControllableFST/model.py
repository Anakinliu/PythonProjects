from torch.utils.data import Dataset
import os
from os import listdir
from os.path import isfile, join
import time
import numpy as np
import sys
import functools
from skimage.transform import resize
from utils import *
import netdef

STROKE_SHORTCUT_DICT = {"768": [False, False], "512": [False, True], "256": [True, False], "interp": [True, True]}
STYLE_LAYERS = ('conv1_1', 'conv2_1', 'conv3_1', 'conv4_1', 'conv5_1')
CONTENT_LAYERS = ('conv4_2')

DEFAULT_RESOLUTIONS = ((768, 768), (512, 512), (256, 256))


class DataLoader(Dataset):
    def __init__(self, args):
        file_names = [join(args.train_path, f) for f in listdir(args.train_path) if
                      isfile(join(args.train_path, f)) and ".jpg" in f]
        self.mscoco_fnames = file_names
        self.train_size = len(file_names)
        self.batch_size = args.batch_size
        self.epochs = 0
        self.nbatches = int(self.train_size / args.batch_size)
        self.batch_idx = 0
        self.perm = np.random.permutation(self.train_size)

        print("[*] 训练集大小: {}".format(self.train_size))
        print("[*] 批次大小: {}".format(self.batch_size))
        print("[*] {} #每个epoch的批次数".format(self.nbatches))

    def __len__(self):
        return self.train_size

    def __getitem__(self, idx):
        return load_image(self.mscoco_fnames[idx])


class Model:
    def __init__(self, sess, args):
        # self.sess = sess
        self.batch_size = args.batch_size
        self._build_model(args)
        # self.saver = tf.train.Saver(max_to_keep=None)

        self.data_loader = DataLoader(args)

    def _build_model(self, args):
        style_highres_img = load_image(args.style, shape=DEFAULT_RESOLUTIONS[1])
        self.style_targets = [
            np.array(style_highres_img.resize((shape[0], shape[1]), resample=Image.BILINEAR), dtype=np.float32)
            for shape in DEFAULT_RESOLUTIONS]

        self.content_input = None
        