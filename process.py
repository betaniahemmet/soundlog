import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
from audiolog import record
import csv
from datetime import datetime, date
import os
import pathlib

todays_date = date.today()
todays_data_path = pathlib.Path.cwd() / 'collected_data' / f'{todays_date}.csv'


def make_csv(max_amp):
    if os.path.isfile(todays_data_path):
        file_exists = True
    else:
        file_exists = False

    print(file_exists)
    with open(todays_data_path, "a") as csv_file:
        fieldnames = ["time", "amp"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        time_now = datetime.now()
        #df['time'] = pd.Series([val.time() for val in df['time']])
        current_time = time_now.strftime("%H:%M:%S")
        if not file_exists:
            writer.writeheader()
        writer.writerow({"time": current_time, "amp": max_amp})

def concat_csv():
    pass


def make_df():
    pass


def read_csv():
    pass


def plot_csv():
    rate = 44100
    # rate, data = wavfile.read('FILE.wav')
    
    # t = np.arange(len(data[:,0]))*1.0/rate
    # plt.plot(t, data[:,0])
    # plt.show()
    pass


def main():
    i = 300
    while i > 1:
        i -= 1
        record()
        rate, data = wavfile.read("FILE.wav")
        max_amp = data.max()
        make_csv(max_amp)
        os.remove("FILE.wav")

if __name__ == "__main__":
    main()
