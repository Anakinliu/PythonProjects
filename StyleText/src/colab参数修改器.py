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
# G_B = "GB_kaiti.ckpt"

# G_B = "GB-erode-yaheiB.ckpt"
G_B = "GB-iccv.ckpt"
# G_B = "GB-erode-kaiti.ckpt"
# G_B = "GB-skelPLUSblur-kaiti.ckpt"
# G_B = "GB-raw-yaheiB.ckpt"
# G_B = "GB_kaiti.ckpt"
# G_B = "GB-no-blur-yaheiB.ckpt"

# test_name = "sha"  # 测试模型时所用文字图像
test_name = "lu"  # 测试模型时所用文字图像
test_file_name = "0730.png"  # 测试模型时所用文字图像的文件名，因为可能是jpg或png
# snowflakes2.jpg
# style_file_name = "maple.png"  # 风格图像的文件名
# style_file_name = "snowflakes3_style.jpg"  # 风格图像的文件名
# style_file_name = "corn4_style.jpg"  # 风格图像的文件名
style_file_name = "728.png"  # 风格图像的文件名

s_angle_jitter = False  # 训练结构时是否抖动角度
t_angle_jitter = False  # 训练纹理时是否抖动角度
use_text_path = False

# s_style_name = "fire-erode-yaheiB"  # 训练结构
# s_style_name = "fire-erode-kaiti"  # 训练结构
s_style_name = "silver-heiA"  # 训练结构
# t_style_name = "fire-erode-yaheiB"  # 训练纹理
# t_style_name = "fire-erode-kaiti"  # 训练纹理
t_style_name = "silver-heiA"  # 训练纹理


if s_angle_jitter:  # 是否抖动角度
    s_style_name += "-S-angle-jitter"  # 结构
if t_angle_jitter:
    t_style_name += "-T-angle-jitter"  # 纹理

x2 = f"""
!python "/content/drive/My Drive/Colab Notebooks/StyleText/src/trainStructureTransfer.py" --style_name "/content/drive/My Drive/Colab Notebooks/StyleText/data/style/{style_file_name}" --batchsize 32 --Straining_num 2560 --step1_epochs 30 --step2_epochs 40 --step3_epochs 80 --scale_num 4 --save_path "/content/drive/My Drive/Colab Notebooks/StyleText/save" --save_name {s_style_name} --gpu --load_GB_name "/content/drive/My Drive/Colab Notebooks/StyleText/save/{G_B}" """
print("训练笔画（结构）的参数：")
if s_angle_jitter:
    print(x2 + " --Sanglejitter")
else:
    print(x2)

print()

# for structure with directional patterns, training without --Sanglejitter will be a good option
x3 = f"""
!python "/content/drive/My Drive/Colab Notebooks/StyleText/src/trainTextureTransfer.py" --style_name "/content/drive/My Drive/Colab Notebooks/StyleText/data/style/{style_file_name}" --batchsize 32 --Ttraining_num 800 --texture_step1_epochs 40 --save_path "/content/drive/My Drive/Colab Notebooks/StyleText/save" --save_name {t_style_name} --gpu --load_GB_name "/content/drive/My Drive/Colab Notebooks/StyleText/save/{G_B}" --load_GS_name "/content/drive/My Drive/Colab Notebooks/StyleText/save/{s_style_name}-GS.ckpt" """
print("训练纹理的参数：")
if t_angle_jitter:
    print(x3 + '--Tanglejitter')
elif use_text_path:
    print(x3 + '--style_loss --text_path "/content/drive/My Drive/Colab Notebooks/StyleText/data/rawtext/yaheiB/train"')
else:
    print(x3)

print()

x1 = f"""
!python "/content/drive/My Drive/Colab Notebooks/StyleText/src/test.py" --text_name "/content/drive/My Drive/Colab Notebooks/StyleText/data/rawtext/kaiti/less/{test_file_name}" --scale -1 --scale_step 0.05 --structure_model "/content/drive/My Drive/Colab Notebooks/StyleText/save/{s_style_name}-GS.ckpt" --texture_model "/content/drive/My Drive/Colab Notebooks/StyleText/save/{t_style_name}-GT.ckpt" --result_dir "/content/drive/My Drive/Colab Notebooks/StyleText/output/{s_style_name}_{t_style_name}-{test_name}" --name {s_style_name}_{t_style_name}-{test_name} --gpu
"""
print('测试')
print(x1)
