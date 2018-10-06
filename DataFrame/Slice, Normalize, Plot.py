#Achieve same function but with less codes
import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="C:\\Users\\jlzxi\\Desktop\\Data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
            dftemp=pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True,
            usecols=['Date','Adj Close'], na_values=['nan'])
            dftemp = dftemp.rename(columns={'Adj Close':symbol})
            df = df.join(dftemp)
            if symbol == 'SPY':
                df = df.dropna(subset=["SPY"])
            

    df = df/df.ix[0] #normalize all data, or df = df/df.ix[0,:]
    return df


def plot_data(df):
    """Plot Stock Prices"""
    ax = df.plot(title= "Stock Prices", fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.grid(True)
    plt.show()
	#can also slice it into data we want by changing the df to contain tha tdata
	#plot the df

def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-22', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']
    
    # Get stock data
    df = get_data(symbols, dates)

    plot_data(df)
    print(df)


if __name__ == "__main__":
    test_run()
