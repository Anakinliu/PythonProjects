from gensim.models import word2vec
import jieba
import numpy as np

from keras.models import model_from_json


def get_vectored_review(data):
    review = []
    for ph in jieba.cut(data, cut_all=False):
        review.append(ph)
    # print("分词 结果：", review)
    max_len = 20
    # 得到word到index的对应
    model = word2vec.Word2Vec.load('model/word_vec_model.model')
    word2index = {token: token_index for token_index, token in enumerate(model.wv.index2word)}
    max_words = len(word2index) + 1  # word2index所有单词
    numize_review = []
    with open("res/stopwords.txt", encoding='utf-8') as f:
        stopWords = [word.replace("\n", "") for word in f.readlines()]
    # print('review', review)
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


def predict(str_review):
    # 在使用加载的模型之前，必须先编译它。这样，使用该模型进行的预测可以使用Keras后端的适当而有效的计算。
    # 加载模型并使用model_from_json创建模型
    json_file = open('model/net_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # 加载权重
    loaded_model.load_weights("model/model_weights.h5")
    print("已加载模型与权重")

    # 编译模型
    loaded_model.compile(optimizer='rmsprop',
                         loss='categorical_crossentropy',
                         metrics=['accuracy'])
    # 不加这句那么Flask线程无法访问tf的默认线程，他会创建新的tf线程
    # 从而报错
    #-------------------------
    # str_review = "不会再买这个品牌的东西了！话不多说，直接上图！"
    # review = ['一星都不想给！商家误导消费者，不会再买这个品牌的东西了！话不多说，直接上图！',
    #       '不好意思这个看错了评错了但也没找到修改办法，这个产品还是很不错的很棒棒，但要注意就是放不下带有USB口比较长的插线板，']
    str_review = str_review.strip()  # 去除两端空格
    # print("评论：", str_review)
    vec = get_vectored_review(str_review)
    result = loaded_model.predict_classes(vec)
    # print("||")
    probs = loaded_model.predict(vec)  # 好中差分别的概率值
    # print("||")
    if result == 0:
        cla = '差评😒'
    elif result == 1:
        cla = '中评😐'
    else:
        cla = '好评👍'
    # print(cla)
    str_probs = []
    for i in probs[0]:
        str_probs.append(str(i))
    return cla, str_probs


# x, y = predict('好评')
# print(type(x))
# print(y)
# print(type(list(y)))