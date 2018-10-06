import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import scipy.optimize as spo
import datetime as dt

def symbol_to_path(symbol, base_dir="C:\\Users\\jlzxi\\Desktop\\Data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'TSX' not in symbols:  # add TSX for reference, if absent
        symbols.insert(0, 'TSX')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'TSX':  # drop dates TSX did not trade
            df = df.dropna(subset=["TSX"])

    return df

def find_portfolio_statistics(allocs, df):

	dfcopy = df.copy()

	# Find cumulative value over time
	df = (df/df.ix[0])
	df = df * allocs
	df = df.sum(axis=1)

	# Compute Portfolio Statistics
	dailyreturns = (df.ix[1:]/df.ix[:-1].values) - 1
	average_daily_return = dailyreturns.mean()
	std_daily_return = dailyreturns.std()
	sharpe_ratio = (252**(1/2.0)) * ((average_daily_return-0)/std_daily_return)

	return (-1 * sharpe_ratio)



def optimize_allocations(sd, ed, symbols, gen_plot):

	dates = pd.date_range(pd.to_datetime(sd), pd.to_datetime(ed))
	df = get_data(symbols, dates)

	initial_guess = []
	bounds = ()
	l = list(bounds)
	for column in df:
		initial_guess.append(1/float(df.shape[1]))
		l.append((0.0,1.0))


	max_result = spo.minimize(find_portfolio_statistics,initial_guess,args=(df),method='SLSQP',bounds=tuple(l))
	print('Allocations for {}: {}'.format(symbols, max_result.x))

	dfcopy = df.copy()
	df_alloc = df * max_result.x

	df_up = df_alloc.sum(axis=1)

	cumulative_return = (df_up.ix[-1]/df_up.ix[0]) - 1
	dailyreturns = (df_up.ix[1:]/df_up.ix[:-1].values) - 1
	average_daily_return = dailyreturns.mean()
	std_daily_return = dailyreturns.std()

	sharpe = find_portfolio_statistics(max_result.x, df) * -1

	print('Cumulative Return: {}; Average Daily Return: {}; Standard Deviation of Daily Returns: {}, Sharpe Ratio: {}'.format(cumulative_return,average_daily_return,std_daily_return,sharpe))


	if gen_plot == True:

    	#Plot portfolio along TSX
	    dfcopynormed = dfcopy['TSX']/dfcopy['TSX'].ix[0]
	    ax = dfcopynormed.plot(title='Daily Portfolio Value and TSX', label='TSX')
	    sumcopy = df_alloc.sum(axis=1)
	    normed = sumcopy/sumcopy.ix[0]
	    normed.plot(label='Portfolio Value', ax=ax)
	    ax.set_xlabel('Date')
	    ax.set_ylabel('Price')
	    ax.legend(loc=2)
	    ax.grid(True)
	    plt.show()


print(optimize_allocations('2017-06-09','2018-07-31',["WEED.TO", 'ACB.TO', 'LEAF.TO', 'AMZN', 'GOOG', 'NVDA', 'AMD', 'INTC', 'GS'], True))


#optimize_allocations(df)

