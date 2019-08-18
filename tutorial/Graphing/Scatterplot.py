"""Plot a histogram"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from util import get_data, plot_data

def daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values)-1
    daily_returns.ix[0,:] = 0
    return daily_returns

def test_run():
    dates = pd.date_range('2017-01-01','2017-12-31')
    symbols = ['TSX', 'ACB.TO', 'WEED.TO']
    df = get_data(symbols, dates)
    dReturns = daily_returns(df)

    #Scatterplot
    dReturns.plot(kind='scatter', x = 'TSX', y = 'ACB.TO')
    dReturns.dropna(inplace=True) #to remove nan values
    beta_ACB,alpha_ACB = np.polyfit(dReturns['TSX'],dReturns['ACB.TO'],1)
    #where dReturns['TSX'] are the x coordinates, where 1 is the degree of fn
    #fn returns two things:1 the polnomial coeffcient, 2. the intercept
    plt.plot(dReturns['TSX'],beta_ACB*dReturns['TSX']+alpha_ACB, '-', color='r')
    #for every value of x that is TSX, find the value of y=mx+b (the second argument), '-' = want a line plot with color red
    plt.show()

    dReturns.plot(kind='scatter', x = 'WEED.TO', y = 'ACB.TO')
    plt.show()

    


if __name__ == "__main__":
    test_run()
