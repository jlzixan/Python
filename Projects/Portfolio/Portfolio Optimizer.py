import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import scipy.optimize as spo

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

    df.dropna(inplace = True)
    
    return df

def normalized(df):
    df = df/df.ix[0]
    return df

def get_dailyReturn(df):
    daily_returns = df.copy()
    daily_returns = (df[1:]/df[:-1].values)-1
    daily_returns = daily_returns[1:]
    return daily_returns

def get_cumReturn(df):
    cum_returns = df.copy()
    cum_returns = cum_returns/cum_returns.ix[0]
    cum_returns = cum_returns[-1] - 1
    return cum_returns

def sharpe(alloc, data):
    df = data.copy()
    df = normalized(df)
    df = df *alloc
    df = df.sum(axis = 1)
    
    dr = get_dailyReturn(df)
    
    sr = -1 * (252**(1/2.0))* (dr.mean()/dr.std())

    return sr


def get_Portfolio(sd, ed, symbols, gen_plot):
    dates = pd.date_range(sd, ed)
    prices_all = get_data(symbols, dates)
    price_Index = prices_all['TSX']

    ini_alloc = []
    bnds = ()
    bnds = list(bnds)
    counter = 0
    for column in prices_all:
        ini_alloc.append(1/float(prices_all.shape[1]))
        bnds.insert(counter,(0.0,1.0))
        counter = counter + 1
    bnds = tuple(bnds)
    conts = ({'type': 'eq',
              'fun': lambda inputs: 1.0 - np.sum(inputs)})


    result = spo.minimize(sharpe, ini_alloc, args = (prices_all), bounds = bnds, constraints = conts, method = 'SLSQP')


    prices_all = prices_all * result.x
    prices_all = prices_all.sum(axis=1)
    
    cr = get_cumReturn(prices_all)
    dr = get_dailyReturn(prices_all)
    adr = dr.mean()
    sddr = dr.std()   

    if gen_plot:
        price_Index = normalized(price_Index)
        prices_all = normalized(prices_all)
        ax = price_Index.plot(title='Portfolio Value and TSX', label = 'TSX')
        prices_all.plot(label='Portfolio', ax=ax)
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        ax.legend(loc='upper left')
        ax.grid(True)
        plt.show()   

    
    return result.x, cr, adr, sddr, result.fun*-1


def test_code():
    start_date = dt.datetime(2017,6,9)
    end_date = dt.datetime(2018,7,31)
    symbols = ["WEED.TO", 'ACB.TO', 'LEAF.TO', 'AMZN']
    gen_plot = True

    alloc, cr, adr, sddr, sr = get_Portfolio(start_date, end_date, symbols, gen_plot)
    print("Allocation for {}: {}".format(symbols, alloc))
    print("Cumulative Return:", cr)
    print("Average Daily Return: ", adr)
    print("Volatility: ", sddr)
    print("Sharpe Ratio ", sr)

if __name__ == "__main__":
    test_code()


    
