# 参数配置
# TODO 从casia数据集修改为revedess数据集

class Config:

    # 数据集路径
    # DATA_PATH = 'Datasets/CASIA/6'
    DATA_PATH = 'Datasets/ravedess'

    # 情感标签
    # ravedess数据集 01 = neutral，02 = calm，03 = happy，04 = sad，05 = angry，06 = fearful，07 = disgust，08 = surprised。
    # CLASS_LABELS = ("angry", "fear", "happy", "neutral", "sad", "surprise")
    CLASS_LABELS = ("neutral", "calm", "happy", "sad", "angry", "fearful", "disgust", "surprised")

    # CLASS_LABELS = ("positive", "negative", "neutral")
    # CLASS_LABELS = ("angry", "boredom", "disgust", "fear", "happy", "neutral", "sad")

    # LSTM 的训练 epoch 数
    epochs = 20

    # Opensmile 标准特征集
    CONFIG = 'IS10_paraling'
    # Opensmile 安装路径
    # OPENSMILE_PATH = '/Users/zou/opensmile-2.3.0'
    # OPENSMILE_PATH = 'X:/SoftOnSSD/opensmile-2.3.0'
    OPENSMILE_PATH = 'X:/SoftOnSSD/opensmile-2.3.0/bin/Win32'
    # 每个特征集的特征数量
    FEATURE_NUM = {
        'IS09_emotion': 384,
        'IS10_paraling': 1582,
        'IS11_speaker_state': 4368,
        'IS12_speaker_trait': 6125,
        'IS13_ComParE': 6373,
        'ComParE_2016': 6373
    }

    # 特征存储路径
    # FEATURE_PATH = 'Features/6-category/'
    FEATURE_PATH = 'Features/8-category/'
    # 训练特征存储路径（Opensmile）
    TRAIN_FEATURE_PATH_OPENSMILE = FEATURE_PATH + 'train_opensmile_ravedess.csv'
    # 预测特征存储路径（Opensmile）
    PREDICT_FEATURE_PATH_OPENSMILE = FEATURE_PATH + 'test_opensmile_ravedess.csv'

    # 训练特征存储路径（librosa）
    TRAIN_FEATURE_PATH_LIBROSA = FEATURE_PATH + 'train_librosa_ravedess.p'
    # 预测特征存储路径（librosa）
    PREDICT_FEATURE_PATH_LIBROSA = FEATURE_PATH + 'test_librosa_ravedess.p'

    # 模型存储路径
    MODEL_PATH = 'Models/'