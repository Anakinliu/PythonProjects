import torch.nn as nn
import torch.nn.functional as F

"""
residual block
"""
class Residual_Block(nn.Module):
    def __init__(self, in_channel, out_channel, kernel_size):
        super(Residual_Block, self).__init__()
        # padding = 1才不会改变 H 和 W
        models = [nn.Conv2d(in_channel, out_channel, kernel_size=kernel_size, padding=1),
                  nn.InstanceNorm2d(out_channel, affine=True),
                  nn.ReLU(),
                  nn.Conv2d(in_channel, out_channel, kernel_size=kernel_size, padding=1),
                  nn.InstanceNorm2d(out_channel, affine=True)]
        self.model = nn.Sequential(*models)

    def forward(self, x):
        # print(f'+Residual_Block: {x.shape};')
        x = x + self.model(x)
        # print(f'-Residual_Block: {self.model(x).shape};')
        return x


"""
style transfer net
"""
class Image_Transform_Net(nn.Module):
    def __init__(self):
        super(Image_Transform_Net, self).__init__()
        low_three = [nn.Conv2d(3, 32, kernel_size=9, stride=1, padding=4),
                     nn.InstanceNorm2d(32, affine=True),
                          nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1),
                     nn.InstanceNorm2d(64, affine=True),
                          nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1),
                     nn.InstanceNorm2d(128, affine=True)]
        residual_blocks = []

        for i in range(5):
            residual_blocks.append(Residual_Block(128, 128, 3))
        high_three = [
            nn.ConvTranspose2d(128, 64, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.InstanceNorm2d(64, affine=True),
            nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.InstanceNorm2d(32, affine=True),
            nn.ConvTranspose2d(32, 3, kernel_size=9, stride=1, padding=4, output_padding=0),
            # nn.Tanh()
        ]
        # self.last3 = nn.ConvTranspose2d(128, 64, kernel_size=3, stride=2, padding=1, output_padding=1)
        # self.last2 = nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1)
        # self.last1 = nn.ConvTranspose2d(32, 3, kernel_size=9, stride=1, padding=4, output_padding=0)

        self.model1 = nn.Sequential(*low_three)
        self.model2 = nn.Sequential(*residual_blocks)
        self.model3 = nn.Sequential(*high_three)

    def forward(self, x):
        x = self.model1(x)
        x = self.model2(x)
        x = self.model3(x)
        # print(f'+last3: {x.shape}')
        # x = self.last3(x)
        # print(f'-last3: {x.shape}')
        # print(f'+last2: {x.shape}')
        # x = self.last2(x)
        # print(f'-last2: {x.shape}')
        # print(f'+last1: {x.shape}')
        # x = self.last1(x)
        # print(f'-last1: {x.shape}')
        return x
