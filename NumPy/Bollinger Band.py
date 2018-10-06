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
    if 'SPY' not in symbols: 
        symbols.insert(0, 'SPY')

    for symbol in symbols:
            dftemp=pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True,
            usecols=['Date','Adj Close'], na_values=['nan'])
            dftemp = dftemp.rename(columns={'Adj Close':symbol})
            df = df.join(dftemp)
            if symbol == 'SPY':
                df = df.dropna(subset=["SPY"])
    
    return df


def plot_data(df):
    """Plot Stock Prices"""
    ax = df.plot(title= "Stock Prices", fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.grid(True)
    plt.show()

def test_run():
    dates = pd.date_range('2010-01-22', '2010-12-31')

    symbols = ['SPY']

    df = get_data(symbols, dates)

    #Plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title='SPY rolling mean', label = 'SPY')

    # Compute rolling mean using a 20-day window
    r = df['SPY'].rolling(window = 20)
    rMean = r.mean()
    rStd = r.std()
    upper = rMean + 2*rStd
    lower = rMean - 2*rStd

    rMean.plot(label='Rolling Mean', ax=ax)
    upper.plot(label='Upper', ax=ax)
    lower.plot(label='Lower', ax=ax)
    ax.legend(loc='upper left')
    

    #http://pandas.pydata.org/pandas-docs/stable/computation.html?highlight=rolling%20statistics#moving-rolling-statistics-moments

    plot_data(df)


if __name__ == "__main__":
    test_run()
