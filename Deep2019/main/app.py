from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
from keras.models import model_from_json
from main.vectorize_review import get_vectored_review
import tensorflow as tf

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
                     loss='categorical_crossentropy',
                     metrics=['accuracy'])

graph = tf.get_default_graph()


def predict(str_review):
    # str_review = "不会再买这个品牌的东西了！话不多说，直接上图！"
    # review = ['一星都不想给！商家误导消费者，不会再买这个品牌的东西了！话不多说，直接上图！',
    #       '不好意思这个看错了评错了但也没找到修改办法，这个产品还是很不错的很棒棒，但要注意就是放不下带有USB口比较长的插线板，']

    vec = get_vectored_review(str_review)
    result = loaded_model.predict_classes(vec)
    if result == 0:
        cla = '差评😒'
    elif result == 1:
        cla = '中评😐'
    else:
        cla = '好评👍'
    # print(cla)
    return cla


app = Flask(__name__)


class HelloForm(Form):
    sayhello = TextAreaField('', [validators.DataRequired()])


@app.route('/')
def index():
    form = HelloForm(request.form)
    print('/')
    return render_template('first_app.html', form=form)


@app.route('/hello', methods=['POST'])
def hello():
    form2 = HelloForm(request.form)
    global graph
    with graph.as_default():
        if request.method == 'POST' and form2.validate():
            review = request.form['sayhello']
            res = predict(review)
            return render_template('hello.html', name=res)
    return render_template('first_app.html', form=form2)


if __name__ == '__main__':
    app.run()
