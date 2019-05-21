import pandas as pd
import os


class CSVHandler:
    def __init__(self):
        self.pre = 'csv/'
        self.count = 0
        self.x = []

    def get_first(self):
        """
        因为可能有新文件加入，所以打开这个html页面时要获取文件个数，文件名
        :return: 一个元组,(csv文件个数, 第一个csv文件的内容)
        """
        for file in os.listdir(self.pre):
            if file.endswith('.csv'):
                # print(file)
                self.x.append(self.pre + file)
                self.count += 1
        # print('the total number of files: ' + str(len(x)))
        # print(x[0])
        first = pd.read_csv(self.x[0], encoding='gbk')
        result = [[c, s] for c, s in zip(first['content'], first['score'])]
        # for c, s in zip(first['content'], first['score']):
        #     print(c, s)
        return self.count, result

    def get_want(self, index=0):
        """

        :param index: 前台发来的index
        :return: 文件名列表x[index] =>[['好评',5],...[]]
        """
        f = pd.read_csv(self.x[index], encoding='gbk')
        # 二维列表
        result = [[c, s] for c, s in zip(f['content'], f['score'])]
        # for c, s in zip(first['content'], first['score']):
        #     print(c, s)
        return result

    # 不用了，前台给index
    # def get_pre(self):
    #     f = pd.read_csv(self.x[index], encoding='gbk')
    #     result = [[c, s] for c, s in zip(f['content'], f['score'])]
    #     # for c, s in zip(first['content'], first['score']):
    #     #     print(c, s)
    #     return result
    #
    #
    # def get_next(self):
    #     first = pd.read_csv(x[0], encoding='gbk')
    #     result = [[c, s] for c, s in zip(first['content'], first['score'])]
    #     # for c, s in zip(first['content'], first['score']):
    #     #     print(c, s)
    #     return count, result

# print(get_first())
