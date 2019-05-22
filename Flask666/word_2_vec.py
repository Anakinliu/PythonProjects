from gensim.models import word2vec
from csv_handler import CSVHandler
from participle import Participle
import numpy as np

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

embedding_dim = 100


class W2V:
    def __init__(self, part):
        self.path = 'model/word_vec_model.model'
        self.part = part

    def convert(self):
        sentences = self.part.get_all()
        # print(sentences)
        sentences = np.ndarray.tolist(sentences)
        # print(sentences)
        model = word2vec.Word2Vec(sentences, hs=1, min_count=10, window=1, size=embedding_dim)
        model.save(self.path)  # 保存模型
        print('saved')
        # print(model.most_similar('插排', topn=1))
        # ----------------------------------------------- #

    def get_fig(self):
        """
        使用了from sklearn.manifold import TSNE
        里面的东西还没搞懂-2019/5/22晚十一点
        :return:
        """
        labels = []
        tokens = []
        model = word2vec.Word2Vec.load(self.path)
        for word in model.wv.vocab:
            print(model[word])
            print(word)
            tokens.append(model[word])
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
# w2v = W2V(t)

