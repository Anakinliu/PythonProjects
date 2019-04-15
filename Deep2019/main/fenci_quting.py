import main.get_text_from_csv as prepare
import jieba
import re
# (data, label) = prepare.getHZCPureTextData()
# review = data[0]
# print(type(" ".join(jieba.cut(review, cut_all=False))))
# for i in jieba.cut(review, cut_all=False):
#     print(i)

def getFenCiHouDeList():
    data, label = prepare.getHZCPureTextData()
    # print('--')
    # print(data[0])  # ok
    # print('--')
    data_fenci = []

    # print(label)

    for review in data:
        sen = []
        for ph in jieba.cut(review, cut_all=False):
            sen.append(ph)
        data_fenci.append(sen)

    # print(type(data_fenci[0]))
    # print(len(data_fenci))
    # print(data_fenci[0])
    return data_fenci, label

# data, labal = getFenCiHouDeList()
# print(len(data))
# print(data[0])
# print(len(data[0]))

# 将data[index]中长度不够的删除
# less_index = []
# for i in range(len(data)):
#     if len(data[i]) < 20:
#         less_index.append(i)
# print(less_index)
# data = [x for x in data if data.index(x) != less_index.pop()]
# for i in less_index:
#     del labal[i]

# print(len(data))
# print(len(labal))

# data = []
#
# a = [1, 2]
# b = [3, 4]
# data.extend(a)
# data.extend(b)
# print(data)

# print(str(data_fenci))
# print('保存分词结果')
# with open('fenci.txt','wb') as fw:
#     for i in range(len(data_fenci)):
#         fw.write(data_fenci[i].encode('gbk'))
#         fw.write('\n'.encode('gbk'))
#
# print("执行word2vec")
# # windows下无法执行
# word2vec.word2vec('fenci.txt', 'test.bin', size=300, verbose=True)