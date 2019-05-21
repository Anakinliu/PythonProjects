from gensim.models import word2vec
import jieba
import numpy as np


def get_vectored_review(data):
    review = []
    for ph in jieba.cut(data, cut_all=False):
        review.append(ph)
    print("分词 结果：", review)
    max_len = 20
    # 得到word到index的对应
    model = word2vec.Word2Vec.load('word_vec_model.model')
    word2index = {token: token_index for token_index, token in enumerate(model.wv.index2word)}
    max_words = len(word2index) + 1  # word2index所有单词
    numize_review = []
    with open("stopwords.txt", encoding='utf-8') as f:
        stopWords = [word.replace("\n", "") for word in f.readlines()]
    print('review', review)
    for word in review:
        if word in stopWords:
            continue
        # 未找到对应word则补“插排”对应的index
        try:
            numize_review.append(word2index[word])
        except KeyError:
            numize_review.append(max_words - 1)
    # 检查长度是否够max_len个
    r_len = len(numize_review)
    while r_len < max_len:  # 不足max_len个长度补上字符"?"的index
        numize_review.append(max_words - 1)
        r_len += 1  # 过长则截取max_len个
    if r_len > max_len:
        numize_review = numize_review[:max_len]
        # print(len())
    return np.asarray([numize_review])  # 必须是二维的哦


# model = word2vec.Word2Vec.load('word_vec_model.model')
# print(model.wv['插排'])