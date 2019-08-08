import pandas as pd
import pickle
import Decision_Stump

df = pd.read_csv("C:\\Users\\jlzxi\\Desktop\\Algorithms\\bank.csv")
X = df.values
names = df.columns.values

y = X[:,-1]
X = X[:,:-1]




#with open("C:\\Users\\jlzxi\\Dropbox\\School\\Undergrad\\Year 6\\CPSC 340\\Assignment\\a1_a5t0b\\data\\citiesSmall.pkl", "rb") as f:
          #dataset = pickle.load(f)

#X = dataset["X"]
#y = dataset["y"]

