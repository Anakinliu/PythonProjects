# import torch
# import torch.nn as nn
#
# STROKE_SHORTCUT_DICT = {"768": [False, False], "512": [False, True], "256": [True, False], "interp": [True, True]}
# STYLE_LAYERS = ('conv1_1', 'conv2_1', 'conv3_1', 'conv4_1', 'conv5_1')
# CONTENT_LAYERS = ('conv4_2')
#
# DEFAULT_RESOLUTIONS = ((768, 768), (512, 512), (256, 256))
#
#
# class Model(nn.Module):
#     def __init__(self):
#         super(Model, self).__init__()
#         # self.optiminzer = torch.optim.Adam()
#         self.max_iter = 2e4
#
#     def forward(self, x):
