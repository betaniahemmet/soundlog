import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from config import collected_data_path
import numpy as np
import datetime

def plot_csv():
"""Really need to clean this up, make plots from different days load and so on, now it just loads the first file that it finds. Also maybe make the time into a time object whaen constructing the csv if possible. Need more data for testing"""

    rate = 44100
    file_paths = collected_data_path.glob("**/*")
    files = [f for f in file_paths if f.is_file()]
    df = pd.read_csv(files[0])
    time = [i for i in df.loc[:,'time']]
    time = [datetime.datetime.strptime(line,"%H:%M:%S") for line in time]
    x = [line for line in time]
    y = [int(i) for i in df.loc[:,"amp"]]
    t = np.arange(len(y))*1.0/rate
    plt.plot(x, y, color = "g", linestyle = 'dashed',
             label = 'Sound volume')
    plt.xticks(rotation = 25)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Data collected')
    plt.grid()
    plt.legend()
    plt.show()
    

def main():
    plot_csv()

if __name__ == "__main__":
    main()
