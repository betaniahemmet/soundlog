import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from config import collected_data_path
import numpy as np
import datetime


def plot_csv():
    """Really need to clean this up, make plots from different days. Sort by weeks and then days? Make interface. Need more data for testing"""

    file_paths = collected_data_path.glob("**/*")
    files = [f for f in file_paths if f.is_file()]
    df = pd.read_csv(files[0])
    time = [i for i in df.loc[:, "time"]]
    
    x = [line for line in time]
    y = [int(i) for i in df.loc[:, "amp"]]
   
    plt.figure(figsize=(15, 8), layout='constrained')
    plt.plot(x, y, color="g", label="Sound volume")
    plt.xticks(x, rotation=25)
    plt.locator_params(nbins=8)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Data collected")
    plt.grid()
    plt.legend()

    plt.show()

def main():
    plot_csv()


if __name__ == "__main__":
    main()
