import pandas as pd
import os
import matplotlib.pyplot as plt


def plot_csv():
    rate = 44100
    # rate, data = wavfile.read('FILE.wav')
    file_paths = .glob("**/*")
    files = [f for f in file_paths if f.is_file()]
    
    df = pd.read_csv(files[0])

    # t = np.arange(len(data[:,0]))*1.0/rate
    # plt.plot(t, data[:,0])
    # plt.show()
    pass

