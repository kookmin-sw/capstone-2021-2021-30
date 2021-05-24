#get mfcc vectors from audio

from google.colab import files
import librosa.display
import librosa
import numpy as np

files.upload()

def make_dataset():
    path = "./testaudio.wav"  # local audio file.
    sample_rate = 12600
    win_length = sample_rate / (1000/20)
    x = librosa.load(path, sample_rate)[0]
    S = librosa.feature.melspectrogram(x, sr=sample_rate, win_length=win_length, hop_length=win_length/2)
    log_S = librosa.power_to_db(S, ref=np.max)
    mfcc = librosa.feature.mfcc(S=log_S, n_mfcc=35)
    delta2_mfcc = librosa.feature.delta(mfcc, order=2)  # audio file is saved after it is vectorized

    return delta2_mfcc
