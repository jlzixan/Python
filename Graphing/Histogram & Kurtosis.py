"""Plot a histogram"""
import pandas as pd
import matplotlib.pyplot as plt

from util import get_data, plot_data

def daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values)-1
    daily_returns.ix[0,:] = 0
    return daily_returns

def test_run():
    dates = pd.date_range('2009-01-01','2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    plot_data(df)

    dReturns = daily_returns(df)
    plot_data(dReturns)

    #Plot histogram
    dReturns.hist(bins=20) 

    #Mean and stats
    mean = dReturns['SPY'].mean()
    std = dReturns['SPY'].std()

    plt.axvline(mean, color='w',linestyle='dashed',linewidth=2)
    plt.axvline(std, color='r',linestyle='dashed',linewidth=2)
    plt.axvline(-std, color='r',linestyle='dashed',linewidth=2)
    plt.show()

    #Compute kurtosis
    print(dReturns.kurtosis())

if __name__ == "__main__":
    test_run()
