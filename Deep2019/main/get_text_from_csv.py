import pandas as pd
import numpy as np

def getHZCPureTextData():
    hp = []
    for i in range(1, 4):
        haoping = pd.read_csv('csv/hao/%d.csv' % i, encoding='gbk')
        for j in list(haoping['content']):
            hp.append(j)
    #print(len(hp))

    zp = []
    for i in range(1, 4):
        zhongping = pd.read_csv('csv/zhong/%d.csv' % i, encoding='gbk')
        for j in list(zhongping['content']):
            zp.append(j)
    #print(len(zp))

    cp = []
    for i in range(1, 3):
        chaping = pd.read_csv('csv/cha/%d.csv' % i, encoding='gbk')
        for j in list(chaping['content']):
            cp.append(j)
    #print(len(cp))

    # 合并好，中，差数据集
    all_review = []
    all_review.extend(hp)
    all_review.extend(zp)
    all_review.extend(cp)
    #print(len(all_review))

    # 建立评级label
    all_score = []
    for i in range(1500):
        all_score.append(2)
    for i in range(1500):
        all_score.append(1)
    for i in range(1000):
        all_score.append(0)

    # 打乱顺序，因为一开始都是好评，接着中评，最后差评，这样在不便于划分测试数据与验证数据据
    indices = np.arange(len(all_score))  # 随机打乱
    np.random.shuffle(indices)
    np_review = np.asarray(all_review)
    np_score = np.asarray(all_score)
    np_review = np_review[indices]
    np_score = np_score[indices]
    all_review = list(np_review)
    all_score = list(np_score)

    return all_review, all_score

# getHZCPureTextData()




