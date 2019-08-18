import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("C:\\Users\\jlzxi\\Desktop\\HCP.csv")
    df['Adj Close'].plot()

    #plt.xlabel('Smarts')
    #plt.ylabel('Probability')
    plt.title('HCP')
    #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    #plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()
	
	df = df/df.ix[0] #normalize


if __name__ == "__main__":
    test_run()

#https://matplotlib.org/users/pyplot_tutorial.html#working-with-text
