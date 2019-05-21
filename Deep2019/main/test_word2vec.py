from gensim.models import word2vec

model = word2vec.Word2Vec.load('word_vec_model.model')
print(model.wv['插排'])

# 与给定文本相似的信息
req_count = 5
for key in model.wv.similar_by_word('插排', topn=100):
    if len(key[0]) >= 1:
        req_count -= 1
        print(key[0], key[1])
        if req_count == 0:
            break

word2index = {token: token_index for token_index, token in enumerate(model.wv.index2word)}
print()
print(model.vocab['插排'].index)
