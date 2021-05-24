import urllib
import numpy as np
import matplotlib.pyplot as plt
import random

import tensorflow as tf
from tensorflow.keras.layers import Embedding , LSTM , Dense , Bidirectional , Flatten
from tensorflow.keras.models import Sequential , load_model
from tensorflow.keras.callbacks import ModelCheckpoint

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
audio_datasets = make_dataset()
label_tmp = make_keypoint_data()

for i in range(234255-234186):
  label_tmp.append(random.random())
labels = np.array(label_tmp , dtype=np.float32)

audio_datasets = np.array(audio_datasets , dtype = np.float32)
scaler.fit(audio_datasets)
audio_datasets = scaler.fit_transform(audio_datasets)
audio_datasets = np.reshape(audio_datasets, (234255,1))


train_size = 150000

train_datas = audio_datasets[:train_size]
train_labels = labels[:train_size]

test_datas = audio_datasets[train_size:]
test_labels = labels[train_size:]

max_len = 150000
embedding_dim = 8 #
keypoint_size = 1697*3
model = Sequential([
    Embedding(keypoint_size,embedding_dim , input_length = max_len),
    Bidirectional(LSTM(64,return_sequences = "True")),
    Bidirectional(LSTM(64)),
    Dense(32, activation = "relu"),
    Dense(1,activation = "sigmoid")
])
#model.summary()

model.compile(optimizer="adam" , loss="binary_crossentropy" , metrics = ["accuracy"])
checkpoint_callback = ModelCheckpoint("test.h5",
                                      save_best_only = True,
                                      monitor = "val_loss",
                                      verbose = 1)
hist = model.fit(train_datas , train_labels,
                 validation_data = (test_datas , test_labels),
                 epochs = 2,
                 callbacks = [checkpoint_callback])

