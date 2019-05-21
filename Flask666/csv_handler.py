import pandas as pd
import os

param_list = {'小米': '4354506',
              '公牛': '492036',
              '良品': '5342704',
              '飞利浦': '4130061'
              }


class CSVHandler:
    def __init__(self):
        self.pre = 'csv/'
        self.count = {}
        self.x = []

    def get_first(self, cla=0):
        """
        因为可能有新文件加入，所以打开这个html页面时要获取文件个数，文件名
        :return: 一个元组,(csv文件个数, 第一个csv文件的内容)
        """
        self.x = []
        # 为None时各个value为三个品牌的所有评论总数
        for k in param_list:
            self.count[k] = 0
        # file: 每个文件的文件名， 不好含路径
        for file in os.listdir(self.pre):
            if file.endswith('.csv'):
                # print(file)
                # print(file[-5])
                if cla is 0:
                    self.x.append(self.pre + file)
                elif cla is int(file[-5]):  # 注意要转为int！！！
                    # 只向x中加入差评
                    self.x.append(self.pre + file)
                    pass
        print(len(self.x))
        for f in self.x:
            for k in param_list:
                if param_list[k] in f:
                    self.count[k] += 1

        first = pd.read_csv(self.x[0], encoding='gbk')
        result = [[c, s] for c, s in zip(first['content'], first['score'])]
        # for c, s in zip(first['content'], first['score']):
        #     print(c, s)
        return self.count, result

    def get_want(self, index=1):
        """
        :param index: 前台发来的index
        :return: 文件名列表x[index] =>[['好评',5],...[]]
        """
        print('index ', index)
        f = pd.read_csv(self.x[index - 1], encoding='gbk')
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


test = CSVHandler()
print(test.get_first(1))
