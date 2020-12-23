"""
import glob
# Importing drive method from colab for accessing google drive
from google.colab import drive
drive.mount('/content/drive/')

"""
# 测试模型时用的参数
"""
{style_name}-GS.ckpt
{test_dis_img}_dis.png
"""
# G_B = "GB_with_no_custom_init.ckpt"
G_B = "GB.ckpt"
# test_name = "sha"  # 测试模型时所用文字图像
test_name = "huo"  # 测试模型时所用文字图像
test_file_name = "huo_dis.png"  # 测试模型时所用文字图像的文件名，因为可能是jpg或png

s_angle_jitter = False  # 训练结构时是否抖动角度
t_angle_jitter = False  # 训练纹理时是否抖动角度

s_style_name = "fire"  # 训练结构
t_style_name = "fire"  # 训练纹理

if s_angle_jitter:  # 是否抖动角度
    s_style_name += "-S-angle-jitter"  # 结构
if t_angle_jitter:
    t_style_name += "-T-angle-jitter"  # 纹理

x1 = f"""
--text_name ../data/oth/words/dis/{test_file_name} --scale -1 --scale_step 0.05 --structure_model ../save/{s_style_name}-GS.ckpt --texture_model ../save/{t_style_name}-GT.ckpt --result_dir ../output/{s_style_name}_{t_style_name}-{test_name} --name {s_style_name}_{t_style_name}-{test_name} --gpu
"""
print(x1)



