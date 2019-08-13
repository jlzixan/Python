#Running DecisionStump on bank.csv
import pandas as pd
import sys
sys.path.insert(1, "C:\\Users\\jlzxi\\Documents\\Github\\Python\\Algorithms")
import utils
import Decision_Stump as ds

list = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome', 'deposit']
df = pd.read_csv("C:\\Users\\jlzxi\\Documents\\Github\\Python\\Algorithms\\bank.csv")

utils.convert_to_categorical(df, list)

X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

model = ds.DecisionStumpErrorRate()
column = model.fit(X,y)
print("Splitting variable is:", df.columns[column])

