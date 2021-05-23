#get mfcc vectors from audio

from google.colab import files
# import librosa.display
# import librosa
import numpy as np
import random

files.upload()


def make_dataset():
    path = "./testaudio.wav"  # local audio file.
    sample_rate = 16000

    x = librosa.load(path, sample_rate)[0]
    S = librosa.feature.melspectrogram(x, sr=sample_rate, win_length=200, hop_length=160)
    log_S = librosa.power_to_db(S, ref=np.max)
    mfcc = librosa.feature.mfcc(S=log_S, n_mfcc=35)
    delta2_mfcc = librosa.feature.delta(mfcc, order=2)  # audio file is saved after it is vectorized

    # datas = []
    # i = 0
    # for each_row in delta2_mfcc:
    #   datas.extend(each_row)
    #   if(i < 6):
    #     datas.append(0)
    #   i+=1

    # return datas
    return delta2_mfcc