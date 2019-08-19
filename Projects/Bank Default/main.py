import pandas as pd
import numpy as np
import utils as utils
from Decision_Tree import DecisionTree
import Decision_Stump as ds
import time as time
from multiprocessing import Pool, cpu_count
from functools import partial

def tree(X,y,i):
    model = DecisionTree(max_depth=i, stump_class=ds.DecisionStumpErrorRate)
    model.fit(X, y)
    y_pred = model.predict(X)
    error = np.mean(y != y_pred)
    print(i, ":", error)


if __name__ == '__main__':
    df = pd.read_csv("bank.csv")
    list = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome', 'deposit']

    utils.convert_to_categorical(df, list)

    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    # Own version

    # depth =  np.array([])
    # error = np.array([])
    #
    # start = time.time()
    # for i in range(10):
    #     print("Depth", i, "\n")
    #     depth = np.append(depth, i)
    #     model = DecisionTree(max_depth=i, stump_class=ds.DecisionStumpErrorRate)
    #     model.fit(X, y)
    #     y_pred = model.predict(X)
    #     e = np.mean(y != y_pred)
    #     error = np.append(error, e)

    # print("Time took:", time.time() - start)
    # print(depth)
    # print(error)
    #
    # model = DecisionTree(max_depth=3, stump_class=ds.DecisionStumpErrorRate)
    # model.fit(X, y)
    # y_pred = model.predict(X)
    # print(np.mean(y != y_pred))

    start = time.time()
    pool = Pool()
    func = partial(tree,X,y)
    pool.map(func, range(10))
    pool.close()
    pool.join()
    print("Time took: ", time.time()-start)