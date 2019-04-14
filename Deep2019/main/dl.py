from keras.models import model_from_json

# 在使用加载的模型之前，必须先编译它。这样，使用该模型进行的预测可以使用Keras后端的适当而有效的计算。
# 加载模型并使用model_from_json创建模型
json_file = open('net_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# 加载权重
loaded_model.load_weights("model_weights.h5")
print("已加载模型与权重")

# evaluate loaded model on test data
loaded_model.compile(optimizer='rmsprop',
                     loss='sparse_categorical_crossentropy',
                     metrics=['accuracy'])

print('my predict:')
# score = net_model.evaluate(x_my_pre, y_my_pre, verbose=0)
# print("%s: %.2f%%" % (net_model.metrics_names[1], score[1]*100))
result = loaded_model.predict_classes(x_my_pre)
data, labels = origin_data.getHZCPureTextData()
print(data[-1], result[0])
# print(len(score))
# print(score[0])
# print(score[1])
print("predict end.")