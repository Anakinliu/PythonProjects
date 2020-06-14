# 训练
# Opensmile 提特征
python3 cmd.py -o t -mt 'svm' -mn 'SVM_OPENSMILE' -l 1 -f 'o'
python3 cmd.py -o t -mt 'mlp' -mn 'MLP_OPENSMILE' -l 1 -f 'o'
python3 cmd.py -o t -mt 'lstm' -mn LSTM_02 -l 0 -f o
# Librosa 提特征
python3 cmd.py -o t -mt 'svm' -mn 'SVM_LIBROSA' -l 1 -f 'l'
python3 cmd.py -o t -mt 'mlp' -mn 'MLP_LIBROSA' -l 1 -f 'l'

# 预测
# Opensmile 提特征
python3 cmd.py -o p -mt 'svm' -mn 'SVM_OPENSMILE' -f 'o' -a 'Test/happy.wav'
python3 cmd.py -o p -mt 'mlp' -mn 'MLP_OPENSMILE' -f 'o' -a 'Test/neutral.wav'
python3 cmd.py -o p -mt 'lstm' -mn 'LSTM_OPENSMILE' -f 'o' -a 'Test/angry.wav'
# Librosa 提特征
python3 cmd.py -o p -mt 'svm' -mn 'SVM_LIBROSA' -f 'l' -a 'Test/surprise.wav'
python3 cmd.py -o p -mt 'mlp' -mn 'MLP_LIBROSA' -f 'l' -a 'Test/sad.wav'
python3 cmd.py -o p -mt 'lstm' -mn 'LSTM_LIBROSA' -f 'l' -a 'Test/fear.wav'

python cmd.py -o p -mt lstm -mn slm_01 -f l -a Test/AudioData/DC/h01.wav


python cmd.py -o p -mt lstm -mn LSTM_03 -f l -a Test/AudioData/DC/01.wav
