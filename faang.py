
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

    # Plot each stock Close column
    for stock in df['Close'].columns:
        plt.plot(df.index, df['Close'][stock], label=stock)

    # Labels, title, legend
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.title(f"Stock Prices as of {df.index[-1].date()}")
    plt.legend()