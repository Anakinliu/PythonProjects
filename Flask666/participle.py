import jieba
from csv_handler import CSVHandler
import pandas as pd
import numpy as np
from threading import Thread
import os


class Participle(Thread):
    def __init__(self, csv_hand):
        """
        :param csv_hand: CSVHandler的一个实例
        """
        # 必须要写的
        Thread.__init__(self)

        # csv_hand时一个CSVHandler实例
        self.csv_hand = csv_hand
        self.all_review = []
        self.all_score = []
        self.pre = 'p/'
        self.f_name = 'participle.csv'
        self.step = 10  # 每次反水的数量
        self.num = 0
        pass

    def read(self):
        # 获取所有文件名
        self.csv_hand.cla_x(0)
        file_names = self.csv_hand.x

        print(len(file_names))
        for file in file_names:
            d = pd.read_csv(file, encoding='gbk')
            len_d = len(d)
            if len_d != 10:  # 有些页不够10条
                print(file)
            for i in range(len_d):
                self.all_review.append(d['content'][i])
                self.all_score.append(d['score'][i])

    def mess(self):
        # 打乱顺序以便训练
        indices = np.arange(len(self.all_score))  # 随机打乱
        np.random.shuffle(indices)
        np_review = np.asarray(self.all_review)
        np_score = np.asarray(self.all_score)
        np_review = np_review[indices]
        np_score = np_score[indices]
        self.all_review = np_review
        self.all_score = np_score

    def cut(self):
        # 让csv_hand的x得到初始化
        if os.path.exists(self.csv_hand.pre + self.pre + self.f_name):
            return
        self.read()  # 读取所有爬取到的数据
        self.mess()  # 打乱顺序
        done_cut = []
        for review in self.all_review:
            sen = []  # 保存分词后的一条评论
            for ph in jieba.cut(review, cut_all=False):
                sen.append(ph)
            # print(sen)
            # df.append(sen, ignore_index=True)
            # print(df)
            done_cut.append(sen)
            pass
        done_cut = np.asarray(done_cut)
        df = pd.DataFrame(done_cut, columns=['participle'])
        df.to_csv(self.csv_hand.pre + self.pre + self.f_name
                  , index=False, encoding='gbk')
        print('已保存分词完的文件')
        # print('done_cut ', len(done_cut))

    def run(self):
        self.cut()

    def get_want_participle(self, start_index):
        ten = pd.read_csv(self.csv_hand.pre + self.pre + self.f_name,
                          encoding='gbk')
        start_index -= 1
        start_index *= 10
        return list(ten['participle'][start_index: start_index + self.step])

    def get_num(self):
        num = pd.read_csv(self.csv_hand.pre + self.pre + self.f_name,
                          encoding='gbk')
        return int(num.count(0))


# hand = CSVHandler()
# t = Participle(hand)

# t.start()
# t.join()
# t.get_want_participle(10)
# print('ok')
# t.get_want_participle(0)
# print(len(t.all_score))
# print(len(t.all_review))
# print(t.all_review[3000])
