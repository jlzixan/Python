#Achieve same function but with less codes
import os
import pandas as pd

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
        if symbol == 'SPY':
            dfIndex = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True,
            usecols=['Date','Adj Close'], na_values=['nan'])
            dfIndex = dfIndex.rename(columns={'Adj Close': symbol})
            df = df.join(dfIndex, how='inner')
        else:
            dftemp=pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True,
            usecols=['Date','Adj Close'], na_values=['nan'])
            dftemp = dftemp.rename(columns={'Adj Close':symbol})
            df = df.join(dftemp)
            

    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-22', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']
    
    # Get stock data
    df = get_data(symbols, dates)

    """Slice by row range (dates) using DataFrame.ix[] selector"""
    print(df.ix['2010-01-01':'2010-01-31'])

    print(" ")
    
    """Slice by Column(symbols)"""
    print(df['GOOG']) #a single lable selects a single column
    print(df[['IBM','GLD']]) #a list of labels selects multiple columns

    print(" ")
    
    """Slicy by row and colum"""
    print(df.ix['2010-01-01':'2010-01-31',['SPY','IBM']])
    
    #print(df)


if __name__ == "__main__":
    test_run()
