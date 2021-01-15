from __future__ import print_function
import torch
from models import SketchModule
from utils import load_image, to_data, to_var, visualize, save_image, gaussian, weights_init, load_train_batchfnames, prepare_text_batch
from options import TrainSketchOptions
import os

# os.environ["CUDA_VISIBLE_DEVICES"] = "0"


def main():
    # parse options
    parser = TrainSketchOptions()
    opts = parser.parse()
    """
    opts.GB_nlayers = 6 生成器的层数
    opts.DB_nlayers = 5 判别器的层数
    opts.GB_nf = 32 生成器第一层中的特征数量
    opts.DB_nf = 32 判别器第一层中的特征数量
    opts.epochs = 3
    """
    # create model
    print('--- create model ---')
    netSketch = SketchModule(opts.GB_nlayers, opts.DB_nlayers, opts.GB_nf, opts.DB_nf, opts.gpu)
    if opts.gpu:
        netSketch.cuda()
    netSketch.init_networks(weights_init)

    netSketch.train()
    # print(netSketch)
    print('--- training ---')
    for epoch in range(opts.epochs):
        itr = 0
        """
        text_path = ../data/rawtext/yaheiB/train
        batchsize = 16
        text_datasize = 708
        Btraining_num = 12800
        """
        # 按批次划分的文件名，没有的文件也不会报错，(trainnum // batch_size) X (batch_size) 矩阵
        f_names = load_train_batchfnames(opts.text_path, opts.batchsize,
                                        opts.text_datasize, trainnum=opts.Btraining_num)
        """
        augment_text_path = ../data/rawtext/augment/
        batchsize = 16
        augment_text_datasize = 5
        """
        f_names2 = load_train_batchfnames(opts.augment_text_path, opts.batchsize,
                                         opts.augment_text_datasize, trainnum=opts.Btraining_num)

        # fnames的每个数组里（即每个批次的）前 (opts.batchsize // 2 - 1) 为增强数据
        for ii in range(len(f_names)):
            f_names[ii][0:opts.batchsize // 2 - 1] = f_names2[ii][0:opts.batchsize // 2 - 1]
        # print(f'fnames2[1]: {fnames2[0]}')  # OK
        for fname in f_names:  # 每次循环是一个批次大小，即fname有batch_size个元素
            itr += 1
            t = prepare_text_batch(fname, anglejitter=True)
            t = to_var(t) if opts.gpu else t
            control_l = [e / 4. - 1. for e in range(0, 9)]
            # t的shape为[batch_size, 3, 256, 256])
            # control_l为[-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0]
            losses = netSketch.one_pass(t, control_l)
            print('Epoch [%d/%d][%03d/%03d]' % (epoch + 1, opts.epochs, itr, len(f_names)), end=': ')
            print('LDadv: %+.3f, LGadv: %+.3f, Lrec: %+.3f' % (losses[0], losses[1], losses[2]))

    print('--- save ---')
    # directory
    torch.save(netSketch.state_dict(), opts.save_GB_name)


if __name__ == '__main__':
    main()
