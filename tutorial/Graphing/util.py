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
            
    return df

def get_dailyReturn(df):
    daily_returns = df.copy() #Copy given DataFrame
    daily_returns[1:] = (df[1:]/df[:-1].values)-1
    #daily_returns = (df/df.shift(1)) -1 #same functionality but with Panda lib
    daily_returns.ix[0,:]= 0
    return daily_returns

def get_cumReturn(df):
    cum_returns = df.copy()
    cum_returns = cum_returns/cum_returns.ix[0]
    return cum_returns


def plot_data(df):
    """Plot Stock Prices"""
    ax = df.plot(title= "Stock Prices", fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.tick_params(axis = 'both', which = 'major', labelsize = 16)
    plt.grid(True)
    plt.show()

def test_run():
    dates = pd.date_range('2010-01-22', '2010-12-31')

    symbols = ['GOOG', 'IBM', 'GLD']
    
    df = get_data(symbols, dates)

    df1 = get_dailyReturn(df)
    df2 = get_cumReturn(df)
    plot_data(df1)
    plot_data(df2)

if __name__ == "__main__":
    test_run()
