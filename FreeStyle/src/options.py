import argparse


class TrainSketchOptions:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        ## Sketch Module
        # data loader related
        self.parser.add_argument('--text_path', type=str, default='../data/rawtext/yaheiB/train',
                                 help='path of the text images')
        self.parser.add_argument('--augment_text_path', type=str, default='../data/rawtext/augment/',
                                 help='path of the augmented text images')
        self.parser.add_argument('--text_datasize', type=int, default=708,
                                 help='how many text images are loaded for training')
        self.parser.add_argument('--augment_text_datasize', type=int, default=5,
                                 help='how many augmented text images are loaded for training')

        # ouptput related
        self.parser.add_argument('--save_GB_name', type=str, default='../save/GB.ckpt',
                                 help='path of the trained model to be saved')

        # model related
        self.parser.add_argument('--GB_nlayers', type=int, default=6, help='number of layers in Generator')
        self.parser.add_argument('--DB_nlayers', type=int, default=5, help='number of layers in Discriminator')
        self.parser.add_argument('--GB_nf', type=int, default=32,
                                 help='number of features in the first layer of the Generator')
        self.parser.add_argument('--DB_nf', type=int, default=32,
                                 help='number of features in the first layer of the Discriminator')
        # trainingg related
        self.parser.add_argument('--epochs', type=int, default=3, help='epoch number')
        self.parser.add_argument('--batchsize', type=int, default=16, help='batch size')
        self.parser.add_argument('--Btraining_num', type=int, default=12800,
                                 help='how many training images in each epoch')
        self.parser.add_argument('--gpu', action='store_true', default=False, help='Whether using gpu')

    def parse(self):
        self.opt = self.parser.parse_args()
        args = vars(self.opt)
        print('--- load options ---')
        for name, value in sorted(args.items()):
            print('%s: %s' % (str(name), str(value)))
        return self.opt
