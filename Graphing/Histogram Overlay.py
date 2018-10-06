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
    dates = pd.date_range('2017-01-01','2017-12-31')
    symbols = ['TSX', 'ACB.TO']
    df = get_data(symbols, dates)
    dReturns = daily_returns(df)

    #Compute and ploy both histograms on same chart
    dReturns['SPY'].hist(bins=20,label = 'TSX')
    dReturns['TSX'].hist(bins=20,label = 'ACB.TO')
    plt.legend(loc='upper left')    
    plt.show()

if __name__ == "__main__":
    test_run()
