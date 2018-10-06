import pandas as pd
#build a dataframe in pandas
def test_run():
    #Define data Range
    start_date='2018-01-22' #specify date range
    end_date='2018-01-26'
    dates=pd.date_range(start_date,end_date)
    #print(dates)

    #Create an empty dataframe
    df1=pd.DataFrame(index=dates) #Build new dataframe with date as index
    #print(df1)

    #Read benchmark data into temp dataframe
    dfIndex = pd.read_csv("C:\\Users\\jlzxi\\Desktop\\Data\\XIU.TO.csv", index_col="Date",parse_dates=True, usecols=['Date','Adj Close'], na_values=['nan'])
    #index_col: otherwise will use row number to merge.
    # parse_dates: Convert DataFrame date into data time index objects/ use date as row num
    #usecolts: want only these columns
    #na_values: convert "NaN" string into number val
    dfIndex = dfIndex.rename(columns={'Adj Close':'TSX'})
    
    #Merge two dataframes using DataFrame.join()
    ##df1 = df1.join(dftemp) df1 as master, merge dftemp into df1
    ##df1 = df1.dropna() drop all NaN values

    df1 = df1.join(dfIndex, how = 'inner') #same result as above two lines, but inner specify:
    #form intersection of calling frame’s index (or column if on is specified) with other frame’s index, preserving the order of the calling’s one

    #Read Individual Stock into DataFrame
    symbols = ['ACB.TO','WEED.TO','XGD.TO']

    for symbol in symbols:
        dftemp = pd.read_csv("C:\\Users\\jlzxi\\Desktop\\Data\\{}.csv".format(symbol),
                             index_col="Date",parse_dates=True, usecols=['Date','Adj Close'], na_values=['nan'])
        dftemp = dftemp.rename(columns={'Adj Close':symbol})
        df1 = df1.join(dftemp)
    
    print(df1)

if __name__ == "__main__":
    test_run()

##Achieve same function but with less codes
##import os
##import pandas as pd
##
##def symbol_to_path(symbol, base_dir="C:\\Users\\jlzxi\\Desktop\\Data"):
##    """Return CSV file path given ticker symbol."""
##    return os.path.join(base_dir, "{}.csv".format(str(symbol)))
##
##
##def get_data(symbols, dates):
##    """Read stock data (adjusted close) for given symbols from CSV files."""
##    df = pd.DataFrame(index=dates)
##    if 'TSX' not in symbols:  # add SPY for reference, if absent
##        symbols.insert(0, 'TSX')
##
##    for symbol in symbols:
##        # TODO: Read and join data for each symbol
##        if symbol == 'TSX':
##            dfIndex = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True,
##            usecols=['Date','Adj Close'], na_values=['nan'])
##            dfIndex = dfIndex.rename(columns={'Adj Close': symbol})
##            df = df.join(dfIndex, how='inner')
##        else:
##            dftemp=pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True,
##            usecols=['Date','Adj Close'], na_values=['nan'])
##            dftemp = dftemp.rename(columns={'Adj Close':symbol})
##            df = df.join(dftemp)
##            
##
##    return df
##
##
##def test_run():
##    # Define a date range
##    dates = pd.date_range('2010-01-22', '2010-01-26')
##
##    # Choose stock symbols to read
##    symbols = ['GOOG', 'IBM', 'GLD']
##    
##    # Get stock data
##    df = get_data(symbols, dates)
##    print(df)
##
##
##if __name__ == "__main__":
##    test_run()
