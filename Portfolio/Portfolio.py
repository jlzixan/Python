import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def symbol_to_path(symbol, base_dir="C:\\Users\\jlzxi\\Desktop\\Data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'TSX' not in symbols:
        symbols.insert(0, 'TSX')

    for symbol in symbols:
            dftemp=pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True,
            usecols=['Date','Adj Close'], na_values=['nan'])
            dftemp = dftemp.rename(columns={'Adj Close':symbol})
            df = df.join(dftemp)
            if symbol == 'TSX':
                df = df.dropna(subset=["TSX"])

    return df


def normalized(df):
    df = df/df.ix[0]
    return df

def get_dailyReturn(df):
    daily_returns = df.copy()
    daily_returns= (df[1:]/df[:-1].values)-1
    daily_returns = daily_returns[1:]
    return daily_returns

def get_cumReturn(df):
    cum_returns = df.copy()
    cum_returns = cum_returns/cum_returns.ix[0]
    return cum_returns

def get_Portfolio(symbols, dates):
    df = get_data(symbols, dates)
    df = normalized(df)
    df.dropna(inplace=True)
    ax = df.plot(title="Stock and Portfolio Values", fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")

    aAlloc = np.array([0.4,0.3,0.15,0.15])
    principal = 1000000
    aAlloc = aAlloc * principal
    port = df*aAlloc
    
    portVal = port.sum(axis=1)
    dReturn = get_dailyReturn(portVal)
    cReturn = get_cumReturn(portVal)

    #portVal.plot(label="Portfolio",ax=ax)
    ax.tick_params(axis = 'both', which = 'major', labelsize = 16)

    print("Portfolio Value:\n",portVal)
    print("Daily Return:\n", dReturn)
    print("Cumulative Return:\n", cReturn)


    eDReturn = dReturn.mean()
    stdReturn = dReturn.std()
    print("Sharpe: ", (252**(1/2.0) * (eDReturn/stdReturn)
    plt.grid(True)
    plt.show()
    
def test_run():
    dates = pd.date_range('2017-06-09', '2018-07-31')
    symbols = ['WEED.TO', 'ACB.TO', 'LEAF.TO']
    
    get_Portfolio(symbols, dates)



if __name__ == "__main__":
    test_run()
