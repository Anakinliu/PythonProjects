from participle import Participle
import numpy as np
import os
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

embedding_dim = 100


class W2V:

    def __init__(self):
        self.path = 'model'

    def convert(self):
        from gensim.models import word2vec
        # 使用分词类的一个静态方法
        sentences = Participle.get_all()
        sentences = np.ndarray.tolist(sentences)
        if os.path.exists(self.path + "word_vec_model.model"):
            model = word2vec.Word2Vec.load(self.path + "word_vec_model.model")
            pass
        else:
            model = word2vec.Word2Vec(sentences, hs=1, min_count=5, window=1, size=embedding_dim)
            model.save(self.path + "/word_vec_model.model")  # 保存模型
        print('saved')

    def sim(self, word):
        # 可能出现keterror！！！
        from gensim.models import word2vec
        model = word2vec.Word2Vec.load(self.path + "/word_vec_model.model")
        try:
            sim_list = model.wv.similar_by_word(word, 100)
        except KeyError:
            sim_list = []
        req_count = 5
        for key in model.wv.similar_by_word(word, topn=100):
            if len(key[0]) >= 1:
                req_count -= 1
                print(key[0], key[1])
                if req_count == 0:
                    break
        # print(type(sim_list))
        # print(sim_list[0])
        return sim_list

    def get_fig(self):
        """
        使用了from sklearn.manifold import TSNE
        里面的东西还没搞懂-2019/5/22晚十一点
        :return:
        """
        labels = []
        tokens = []
        for word in self.model.wv.vocab:
            print(self.model[word])
            print(word)
            tokens.append(self.model[word])
            labels.append(word)

        tsne_model = TSNE(perplexity=40, n_components=3,
                          init='pca', n_iter=2500, random_state=23)
        new_values = tsne_model.fit_transform(tokens)

        x = []
        y = []
        for value in new_values:
            x.append(value[0])
            y.append(value[1])

        fig = plt.figure(figsize=(32, 32))
        for i in range(len(x)):
            plt.scatter(x[i], y[i])
            plt.annotate(labels[i],
                         xy=(x[i], y[i]),
                         xytext=(5, 2),
                         textcoords='offset points',
                         ha='right',
                         va='bottom')
        # plt.show()
        return fig


# hand = CSVHandler()
# t = Participle(hand)
# w2v = W2V()
# w2v.convert()
# w2v.sim('飞利浦')
