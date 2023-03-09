import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
from soundlog import record
import csv
from datetime import datetime, date
import os
import pathlib
import pandas as pd

todays_date = date.today()
this_week = todays_date.isocalendar()[1]
this_week_path = pathlib.Path.cwd() / "collected_data" / f"{this_week}" # TODO: make paths global
todays_data_path = pathlib.Path.cwd() / "collected_data" / f"{this_week}" / f"{todays_date}.csv"


def make_csv(max_amp):
    if not os.path.exists(this_week_path):
        os.makedirs(this_week_path)
    if os.path.isfile(todays_data_path):
        file_exists = True
    else:
        file_exists = False

    with open(todays_data_path, "a") as csv_file:
        fieldnames = ["time", "amp"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        current_time = datetime.now()
        current_time = current_time.time().replace(microsecond=0)
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
    i = 2
    print(todays_data_path)
    while i > 1:
        i -= 1
        record()
        rate, data = wavfile.read("FILE.wav")
        max_amp = data.max()
        make_csv(max_amp)
        os.remove("FILE.wav")


if __name__ == "__main__":
    main()
