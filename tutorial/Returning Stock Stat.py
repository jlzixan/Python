import pandas as pd

def get_max_close(symbol):
    df = pd.read_csv("C:\\Users\\jlzxi\\Desktop\\{}.csv".format(symbol)) #reading wilde card
    return df['Volume'].mean()

def test_run():
    for symbol in ['HCP']: #add more company names to read more files
        print("Max Close")
        print(symbol,get_max_close(symbol))


if __name__ == "__main__":
    test_run()
