import imageio
import os
import re

SOURCE_DIR = '../output/对比/sakura/sakura-GB-erode-kaiti_sakura-GB-erode-kaiti-lu/'
# print(os.listdir(SOURCE_DIR))


def pics2gif(source_dir):
    """
    :param source_dir: 包含若干以非gif结尾的图片文件
    :return: # 保存动图all.gif到source_dir
    """
    images = []

    file_names = []
    for file_name in os.listdir(source_dir):
        if not file_name.endswith(".gif"):
            file_names.append(file_name)
    # # 需要按照文件名排序！！！有的图片本身就是数字代号。。。故正则里考虑到.
    file_names = sorted(file_names, key=lambda x: int(re.search('[0-9]+\\.', x).group()[:-1]))
    # print(file_names)
    for filename in file_names:
        images.append(imageio.imread(f'{source_dir}{filename}'))
    imageio.mimsave(f'{source_dir}all.gif', images)
    print(f'{source_dir}all.gif 已保存！')


pics2gif(SOURCE_DIR)
# x = 'fire-0745_11.png'
# print(re.search('[0-9]+\\.', x).group())