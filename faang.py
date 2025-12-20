#!/usr/bin/env python3
# We are adding this line directly saying the interpreter to use python3


# Import necessary libraries.
import datetime as dt
import os
import pandas as pd
import matplotlib.pyplot as plt 





def plot_data():
    """
    Reads the latest CSV from 'data', plots Close prices of all stocks,
    and saves the plot in 'plots' folder with timestamp.
    """

    # Get all CSV files in the data folder
    files = [f for f in os.listdir('data') if f.endswith('.csv')]
    files.sort()  # sort alphabetically, last one is latest
    latest_file = files[-1]

    # Load CSV into DataFrame
    df = pd.read_csv(os.path.join('data', latest_file), header=[0,1], index_col=0, parse_dates=True)

    # Create a figure
    plt.figure(figsize=(10,6))

    # Plot Close prices (explicitly for clarity)
    plt.plot(df.index, df["Close"]["META"], label="META")
    plt.plot(df.index, df["Close"]["AAPL"], label="AAPL")
    plt.plot(df.index, df["Close"]["AMZN"], label="AMZN")
    plt.plot(df.index, df["Close"]["NFLX"], label="NFLX")
    plt.plot(df.index, df["Close"]["GOOG"], label="GOOG")

    # Labels, title, legend
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title(f"Stock Prices as of {df.index[-1].date()}")
    plt.legend()

    # Plotting.
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    plt.savefig("plots/" + timestamp + ".png")
    plt.close()
    

# This line means that the following code will only run if this script is executed directly, it wont run if this script is imported as a module in another script.
if __name__ == "__main__":
    plot_data()
