import urllib
import numpy as np
import matplotlib.pyplot as plt
import random
import librosa
import tensorflow as tf
from tensorflow.keras.layers import Embedding , LSTM , Dense , Flatten
from tensorflow.keras.models import Sequential , load_model
from tensorflow.keras.callbacks import ModelCheckpoint
from sklearn.preprocessing import MinMaxScaler
from keras.preprocessing.sequence import pad_sequences

scaler = MinMaxScaler()
audio_datas = make_dataset()
labels = make_keypoint_data()
for i in range(26):
  labels.pop()
#labels = change_onehot(labels)
# audio_datas = scaler.fit_transform(audio_datas)

#make labels datas being placed bwteen 0 ~ 29
for i in range(len(labels)):
  if labels[i] < 0: labels[i] +=30
labels = np.array(labels)


processed_audio_datas = audio_preprocessing(audio_datas)
processed_audio_datas = np.array(processed_audio_datas)

audio_datas = processed_audio_datas
scaler = MinMaxScaler()
audio_datas = scaler.fit_transform(audio_datas)
#padding
audio_datas = pad_sequences(audio_datas , maxlen=30,padding='post', truncating='post')

train_size = 200000

train_datas =audio_datas[:train_size]
train_labels= labels[:train_size]
test_datas = audio_datas[train_size:60000]
test_labels= labels[train_size:60000]

max_len = 30
embedding_dim =2#
keypoint_size = 30
model = Sequential([
    Embedding(keypoint_size,embedding_dim , input_length = max_len),
    LSTM(64,return_sequences="True"),
    Flatten(input_shape = (1,30)),
    Dense(30,activation='softmax')
])
#model.summary()

#activative function -> softmax (has 30 classes) , loss function -> sparse_categorical_crossentropy ( each value of labels are integer (0~29))
model.compile(optimizer="adam" , loss="sparse_categorical_crossentropy" , metrics = [tf.keras.metrics.SparseCategoricalAccuracy()])

checkpoint_callback = ModelCheckpoint("test.h5",
                                      save_best_only = True,
                                      monitor = "val_loss",
                                      verbose = 1)
hist = model.fit(train_datas , train_labels, epochs = 2)

