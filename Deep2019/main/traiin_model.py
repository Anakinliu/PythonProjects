import main.fenci_quting as fenci
import main.get_text_from_csv as origin_data
import os
import numpy as np
from gensim.models import word2vec

from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense, Dropout, Activation, LSTM

from keras.utils.np_utils import to_categorical

sentences, labels = fenci.getFenCiHouDeList()


# min_count指定了需要训练词语的最小出现次数，默认为5
# size指定了训练时词向量维度，默认为100
# hs: 即我们的word2vec两个解法的选择了，如果是0， 则是Negative Sampling，是1的话并且负采样个数negative大于0，
# (negative默认值时5)则是Hierarchical Softmax。默认是0即Negative Sampling。


if os.path.exists('word_vec_model.model'):
    model = word2vec.Word2Vec.load('word_vec_model.model')
else:
    model = word2vec.Word2Vec(sentences, hs=1, min_count=5, window=1, size=100)
    model.save('word_vec_model.model')  # 保存模型

# 与给定文本相似的信息
# req_count = 5
# for key in model.wv.similar_by_word('插排', topn = 100):
#     if len(key[0]) >= 2:
#         req_count -= 1
#         print(key[0], key[1])
#         if req_count == 0:
#             break


# print(type(model.wv['插排']))
# print(model.wv['插排'])

# print((model.wv['插排'] == model.wv['插排']).all())  # True


embedding_dim = 100  # 与word2vec构造函数中的size相同
max_len = 20  # 每个评论截取前20个
training_samples = 3000
val_samples = 1000


# 得到word到index的对应
word2index = {token: token_index for token_index, token in enumerate(model.wv.index2word)}
max_words = len(word2index)  # word2index所有单词
# print(len(word2index))  # 7132
embedding_matrix = np.zeros((max_words, embedding_dim))
for word, i in word2index.items():
    if i < max_words:
        embedding_vector = model.wv[word]
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector

print(word2index['。'])
# 首先将评论中文根据word2vec将分词后的汉字转化为数字
numize_data = []
numize_review = []
with open('stopwords.txt', encoding='utf-8') as f:
    stopWords = [word.replace("\n", "") for word in f.readlines()]
for review in sentences:
    numize_review = []
    for word in review:
        if word in stopWords:
            print(word)
            continue
        # 未找到对应word则补“插排”对应的index
        try:
            numize_review.append(word2index[word])
        except KeyError:
            numize_review.append(word2index['？'])
    r_len = len(numize_review)
    while r_len < max_len:  # 不足max_len个长度补上字符"."的index
        numize_review.append(word2index['。'])
        r_len += 1  # 过长则截取max_len个
    if r_len > max_len:
        numize_review = numize_review[:max_len]
    numize_data.append(numize_review)

print(numize_data[0])
print(len(numize_data))
print('Done--1')

# 向量化review与label
numize_data = np.asarray(numize_data)
labels = np.asarray(labels)
# one-hot 编码， 即分类编码
one_hot_label = to_categorical(labels)
print('----------one_hot_label shape: ' + str(one_hot_label.shape))
# 分开训练集与验证集
x_train = numize_data[:training_samples]
y_train = one_hot_label[:training_samples]
x_val = numize_data[training_samples:training_samples + val_samples]
y_val = one_hot_label[training_samples:training_samples + val_samples]
# x_my_pre = numize_data[-1:]
# y_my_pre = one_hot_label[-1:]
print('Done--2')
# print('type info:')
# print(x_train)
# print(type(x_train))


# 定义模型
net_model = Sequential()
net_model.add(Embedding(max_words, embedding_dim, input_length=max_len))

# 密集连接网络
# net_model.add(Flatten())
# net_model.add(Dense(32, activation='relu'))
# net_model.add(Dense(4, activation='softmax'))
# net_model.summary()  # 打印一系列此网络的总结信息

# LSTM算法
net_model.add(LSTM(output_dim=50))
net_model.add(Dropout(0.5))

net_model.add(Dense(3, activation='softmax'))
net_model.summary()

# 在模型中加载word2vec嵌入Embedding层中
net_model.layers[0].set_weights([embedding_matrix])
# 冻结第一层， 因为它已经训练完了
net_model.layers[0].trainable = False

net_model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

histroy = net_model.fit(x_train,
                        y_train,
                        epochs=5,
                        batch_size=64,
                        validation_data=(x_val, y_val))
print('Done--end')

# print('my predict:')
# score = net_model.evaluate(x_my_pre, y_my_pre, verbose=0)
# print("%s: %.2f%%" % (net_model.metrics_names[1], score[1]*100))
# result = net_model.predict_classes(x_my_pre)
# data, labels = origin_data.getHZCPureTextData()
# print(type(result))
# print(len(result))
# print(len(score))
# print(score[0])
# print(score[1])
print("predict end.")

# 序列化模型并保存到JSON文件中
model_json = net_model.to_json()
with open("net_model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
net_model.save_weights("model_weights.h5")
print("已保存模型与权重到文件中")


# 显示"插排"的近似词
# req_count = 5
# for key in model.wv.similar_by_word('插排', topn =100):
#     if len(key[0]) >= 2:
#         req_count -= 1
#         print(key[0], key[1])
#         if req_count == 0:
#             break

# 已得到word2index， 弃用
# if os.path.exists('embedding_matrix.npy'):
#     embedding_matrix = np.load("embedding_matrix.npy")
# else:
#     n = 0
#     for a_review in sentences:
#         print(a_review)
#         review_count = 0
#         for fenci_word in a_review:
#             if not model.wv[fenci_word] in embedding_matrix and review_count <= 20:
#                 embedding_matrix[] = model.wv[fenci_word]
#                 n += 1
#                 review_count += 1
#         if n >= max_words:
#             break
#     np.save("embedding_matrix.npy", embedding_matrix)
#----------

# embedding_matrix[0] = model.wv['插排']
# if model.wv['插排'] in embedding_matrix:  # True
#     print(233)
# word2index = {token: token_index for token_index, token in enumerate(model.wv.index2word)}

# print(model.wv[','])
# print(word2index['插排'])  # True
print('Done')
# print(embedding_matrix[0])

# print(len(sentences))
#print(len(embedding_matrix[0]))  # 100



