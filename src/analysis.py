import pandas as pd
import matplotlib.pyplot as plt

def plot_time_series(df, column="Close"):
    df[column].plot(figsize=(10,5))
    plt.title(f"{column} Price Trend")
    plt.show()
