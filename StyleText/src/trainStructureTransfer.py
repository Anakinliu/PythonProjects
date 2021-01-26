from __future__ import print_function
import torch
from models import SketchModule, ShapeMatchingGAN
from utils import  to_var,    weights_init
from utils import load_train_batchfnames, prepare_text_batch, load_style_image_pair, cropping_training_batches
import random
from options import TrainShapeMatchingOptions


# os.environ["CUDA_VISIBLE_DEVICES"] = "0"

"""
!python "/content/drive/My Drive/Colab Notebooks/StyleText/src/trainStructureTransfer.py" 
--style_name "/content/drive/My Drive/Colab Notebooks/StyleText/data/style/flower3_style.jpg" 
--batchsize 32 
--Straining_num 2560 
--step1_epochs 30 
--step2_epochs 40 
--step3_epochs 80 
--scale_num 4 
--save_path "/content/drive/My Drive/Colab Notebooks/StyleText/save" 
--save_name flower3 
--gpu 
--load_GB_name "/content/drive/My Drive/Colab Notebooks/StyleText/save/GB.ckpt"
"""
def main():
    # parse options
    parser = TrainShapeMatchingOptions()
    opts = parser.parse()

    # create model
    print('--- create model ---')
    # 6,4,32,32，6,4,32,32，False
    netShape_M_GAN = ShapeMatchingGAN(opts.GS_nlayers, opts.DS_nlayers, opts.GS_nf, opts.DS_nf,
                                 opts.GT_nlayers, opts.DT_nlayers, opts.GT_nf, opts.DT_nf, opts.gpu)
    # 6, 5, 32, 32
    netSketch = SketchModule(opts.GB_nlayers, opts.DB_nlayers, opts.GB_nf, opts.DB_nf, opts.gpu)

    if opts.gpu:
        netShape_M_GAN.cuda()
        netSketch.cuda()
    netShape_M_GAN.init_networks(weights_init)
    netShape_M_GAN.train()

    netSketch.load_state_dict(torch.load(opts.load_GB_name))
    netSketch.eval()  # 不训练SketchModule

    print('--- training ---')
    # load image pair
    scales = [l * 2.0 / (opts.scale_num - 1) - 1 for l in range(opts.scale_num)]  # opts.scale_num默认值 4
    # [-1.0, -0.33333333333333337, 0.33333333333333326, 1.0]

    # 使用已训练的 netSketch！！！
    Xl, X, _, Noise = load_style_image_pair(opts.style_name, scales, netSketch, opts.gpu)
    """
    Xl: 经过SketchModule的不同模糊程度的 4 个（scale_num默认值 4）距离图像 X
    Xl[0] -- scales[0] -- -1.0
    Xl[3] -- scales[3] -- 1.0
    X：风格图像的距离图像  shape [1, 3, 740图像高度, 1000图像宽度]
    Noise： 噪声？均值.0，方差.2，shape [1, 3, 740图像高度, 1000图像宽度]
    """
    Xl = [to_var(a) for a in Xl] if opts.gpu else Xl
    X = to_var(X) if opts.gpu else X
    Noise = to_var(Noise) if opts.gpu else Noise

    for epoch in range(opts.step1_epochs):  # 默认 30
        for i in range(opts.Straining_num // opts.batchsize):  # 2560 // 32 = 80
            # 论文5.1 ：首先以固定的 l=1 训练G_S ，以学习最大变形。。。。。。。。
            idx = opts.scale_num - 1  # 3
            xl, x = cropping_training_batches(Xl[idx], X, Noise, opts.batchsize,
                                              opts.Sanglejitter, opts.subimg_size, opts.subimg_size)
            # xl与x裁剪的坐标是相同的。
            # xl是加入了一些噪声的自Xl[idx]随机裁剪出的 32 个 大小为 256x256 的xl图像 [32, 3, 256, 256]
            # x就是输入的Output的随机裁剪/选择后的结果，也就是原距离图像随机裁剪/选择后的，与 xl shape 相同 [32, 3, 256, 256]

            losses = netShape_M_GAN.structure_one_pass(x, xl, scales[idx])
            print('Step1, Epoch [%02d/%02d][%03d/%03d]' % (epoch + 1, opts.step1_epochs, i + 1,
                                                           opts.Straining_num // opts.batchsize), end=': ')
            print('LDadv: %+.3f, LGadv: %+.3f, Lrec: %+.3f, Lgly: %+.3f' % (losses[0], losses[1], losses[2], losses[3]))

    netShape_M_GAN.G_S.myCopy()

    for epoch in range(opts.step2_epochs):  # 40
        for i in range(opts.Straining_num // opts.batchsize):  # 2560 // 32 = 80
            idx = random.choice([0, opts.scale_num - 1])  # 0 或 3
            xl, x = cropping_training_batches(Xl[idx], X, Noise, opts.batchsize,
                                              opts.Sanglejitter, opts.subimg_size, opts.subimg_size)
            losses = netShape_M_GAN.structure_one_pass(x, xl, scales[idx])
            print('Step2, Epoch [%02d/%02d][%03d/%03d]' % (epoch + 1, opts.step2_epochs, i + 1,
                                                           opts.Straining_num // opts.batchsize), end=': ')
            print('LDadv: %+.3f, LGadv: %+.3f, Lrec: %+.3f, Lgly: %+.3f' % (losses[0], losses[1], losses[2], losses[3]))

    for epoch in range(opts.step3_epochs):
        for i in range(opts.Straining_num // opts.batchsize):
            idx = random.choice(range(opts.scale_num))  # 0,1,2,3
            xl, x = cropping_training_batches(Xl[idx], X, Noise, opts.batchsize,
                                              opts.Sanglejitter, opts.subimg_size, opts.subimg_size)
            losses = netShape_M_GAN.structure_one_pass(x, xl, scales[idx])
            print('Step3, Epoch [%02d/%02d][%03d/%03d]' % (epoch + 1, opts.step3_epochs, i + 1,
                                                           opts.Straining_num // opts.batchsize), end=': ')
            print('LDadv: %+.3f, LGadv: %+.3f, Lrec: %+.3f, Lgly: %+.3f' % (losses[0], losses[1], losses[2], losses[3]))

    # glyph_preserve 默认False,如果是True那么复杂结构字的论文效果会比不加更好吗？
    if opts.glyph_preserve:
        fnames = load_train_batchfnames(opts.text_path, opts.batchsize,
                                        opts.text_datasize, opts.Straining_num)
        for epoch in range(opts.step4_epochs):
            itr = 0
            for fname in fnames:
                itr += 1
                t = prepare_text_batch(fname, anglejitter=False)
                idx = random.choice(range(opts.scale_num))
                xl, x = cropping_training_batches(Xl[idx], X, Noise, opts.batchsize,
                                                  opts.Sanglejitter, opts.subimg_size, opts.subimg_size)
                t = to_var(x) if opts.gpu else t
                losses = netShape_M_GAN.structure_one_pass(x, xl, scales[idx], t)
                print('Step4, Epoch [%02d/%02d][%03d/%03d]' % (epoch + 1, opts.step4_epochs, itr + 1,
                                                               len(fnames)), end=': ')
                print('LDadv: %+.3f, LGadv: %+.3f, Lrec: %+.3f, Lgly: %+.3f' % (
                losses[0], losses[1], losses[2], losses[3]))

    print('--- save ---')
    # directory
    netShape_M_GAN.save_structure_model(opts.save_path, opts.save_name)


if __name__ == '__main__':
    main()
