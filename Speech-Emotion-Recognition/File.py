# 数据集整理

import os
import shutil

from Config import *
DATA_PATH = r"Datasets\ravedess"


# 批量删除指定路径下所有非.wav文件
def remove(file_path):
    for root, dirs, files in os.walk(file_path):
        # print(root, dirs, files)
        for item in files:
            if not item.endswith('.wav'):
                try:
                    print("Delete file: ", os.path.join(root, item))
                    os.remove(os.path.join(root, item))
                except:
                    continue

# remove(DATA_PATH)  # DONE

# ravedess用不着了
# 批量按指定格式改名（不然把相同情感的音频整理到同一个文件夹时会重名）
def rename(file_path):
    for root, dirs, files in os.walk(file_path):
        for item in files:
            if item.endswith('.wav'):
                # people_name = root.split('/')[-2]
                people_name = root.split('-')[-1]
                # emotion_name = root.split('/')[-1]
                emotion_name = root.split('-')[2]
                item_name = item[:-4]  # 音频原名（去掉.wav）
                old_path = os.path.join(root, item)
                new_path = os.path.join(root, item_name + '-' + emotion_name + '-' + people_name + '.wav')  # 新音频地址
                try:
                    os.rename(old_path, new_path)
                    print('converting ', old_path, ' to ', new_path)
                except:
                    continue


# 把音频按情感分类，复制放在不同文件夹下
def move(file_path):
    for root, dirs, files in os.walk(file_path):
        # print('root', root)
        # print('dirs', dirs)
        # print('files', files)
        for item in files:
            if item.endswith('.wav'):
                print(item)
                # ravedess数据集第三个数字表示情感种类,注意去掉 0
                emotion_name = Config.CLASS_LABELS[int(item[:-4].split('-')[2]) - 1]
                emotion_dir = os.path.join(file_path, str(emotion_name))
                if not os.path.exists(emotion_dir):
                    os.mkdir(emotion_dir)
                # print(emotion_name)
                old_path = os.path.join(root, item)
                # print(old_path)
                new_path = os.path.join(file_path, str(emotion_name), item)
                # new_path = file_path + '\' + emotion_name + '\' + item
                print(new_path)
                try:
                    shutil.copy(old_path, new_path)
                    print("Move ", old_path, " to ", new_path)
                except OSError:
                    print('os error')

move(DATA_PATH)
