import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from config import collected_data_path
import numpy as np
import datetime
import pathlib

def plot_csv(file_path):
    """Really need to clean this up, make plots from different days. Sort by weeks and then days? Make interface. Need more data for testing"""

    df = pd.read_csv(file_path)
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

def get_date(file_name):
    file_name_parts = str(file).split('\\')
    file_name = file_name_parts[-1]
    file_name = file_name.split('.')
    file_name = file_name[0].split('-')
    year = int(file_name[0])
    month = int(file_name[1])
    day = int(file_name[2])
    date = datetime.date(year, month, day)
    return date

def menu():
    print("Vi har samlat data i följande veckor:")
    folder_paths = collected_data_path.glob("*")
    #  _paths = collected_data_path.glob("**/*")
    folders = [str(f) for f in folder_paths if f.exists()]
    recorded_weeks = [f.split('\\')[-1] for f in folders]
    for i in recorded_weeks:
        print(*recorded_weeks)

    print("Skriv den vecka som du vill plotta och tryck sedan enter")
    selected_week = input()
    dates = pathlib.Path.cwd() / "collected_data"  / selected_week # TODO: Clean up paths, make global
    print(dates)
    
    """
    files = [f for f in file_paths if f.is_file()]

    weeks = []

    for file in file_paths:
        date = get_date(file)
        week = date.isocalendar()[1]
        weeks.append(week)
    """
def main():


    menu()


if __name__ == "__main__":
    main()
