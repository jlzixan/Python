import pandas as pd

def test_run():
    df = pd.read_csv("C:\\Users\\jlzxi\\Desktop\\HCP.csv")
    print(df.head())


if __name__ == "__main__":
    test_run()
    
	
#Leeting user to specify which file to load in	
# import pandas as pd

# def get_max_close(symbol):
    # df = pd.read_csv("C:\\Users\\jlzxi\\Desktop\\Data\\{}.csv".format(symbol))
    # return df['Adj Close'].max()

# def test_run():
    # stock_list = input("Enter Stocks List:")
    # stock_list = stock_list.split(',')

    # for symbol in stock_list:
        # print(symbol, " Max Close: ", get_max_close(symbol))

# if __name__ == "__main__":
    # test_run()
