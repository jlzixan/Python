import numpy as np
from scipy import stats


def mode(y):
    if len(y) == 0:
        return -1
    else:
        return stats.mode(y.flatten())[0][0]


class DecisionStumpEquality:

    def __init__(self):
        pass

    def fit(self, X, y):
        N, D = X.shape

        # Get an array with the number of 0's, number of 1's, etc.
        count = np.bincount(y)

        # Get the index of the largest value in count.
        # Thus, y_mode is the mode (most popular value) of y
        y_mode = np.argmax(count)

        self.splitSatisfied = y_mode
        self.splitNSatisfied = None
        self.splitVariable = None
        self.splitValue = None

        if np.unique(y).size <= 1:
            return

        minError = np.sum(y != y_mode)

        # Loop over features looking for the best split
        X = np.round(X)

        for d in range(D):
            for n in range(N):
                # Choose value to equate to
                value = X[n, d]

                # Find most likely class for each split
                y_sat = mode(y[X[:, d] == value])
                y_not = mode(y[X[:, d] != value])

                # Make predictions
                y_pred = y_sat * np.ones(N)
                y_pred[X[:, d] != value] = y_not

                errors = np.sum(y_pred != y)

                if errors < minError:
                    print("New error", minError)
                    minError = errors
                    self.splitValue = value
                    self.splitVariable = d
                    self.splitSatisfied = y_sat
                    self.splitNSatisfied = y_not

        print("Splitting variable: ", self.splitVariable, "\n", "Splitting value: ", self.splitValue)

    def predict(self, X):
        M, D = X.shape
        X = np.round(X)

        if self.splitVariable is None:
            return self.splitSatisfied * np.ones(M)

        yhat = np.zeros(M)

        for m in range(M):
            if X[m, self.splitVariable] == self.splitValue:
                yhat[m] = self.splitSatisfied
            else:
                yhat[m] = self.splitNSatisfied
        return yhat


class DecisionStumpErrorRate:

    def __init__(self):
        pass

    def fit(self, X, y):
        N, D = X.shape

        # must have a minimum of 2 bins
        count = np.bincount(y)

        y_mode = np.argmax(count)

        self.splitSatisfied = y_mode
        self.splitNSatisfied = None
        self.splitVariable = None
        self.splitValue = None

        if np.unique(y).size <= 1:
            return

        minError = np.sum(y != y_mode)
        


        for d in range(D):
            for n in range(N):
                value = X[n, d]

                y_sat = mode(y[X[:, d] > value])
                y_not = mode(y[X[:, d] <= value])

                y_pred = y_sat * np.ones(N)
                y_pred[X[:, d] <= value] = y_not

                errors = np.sum(y_pred != y)

                if errors < minError:
                    #print("Model Errors", errors)
                    minError = errors
                    self.splitVariable = d
                    self.splitValue = value
                    self.splitSatisfied = y_sat
                    self.splitNSatisfied = y_not
                    
        return self.splitVariable
        
    def predict(self, X):
        M, D = X.shape

        if self.splitVariable is None:
            return self.splitSatisfied * np.ones(M)

        yhat = np.zeros(M)

        for m in range(M):
            if X[m, self.splitVariable] > self.splitValue:
                yhat[m] = self.splitSatisfied
            else:
                yhat[m] = self.splitNSatisfied

        return yhat


class DecisionStumpInfoGain(DecisionStumpErrorRate):
    def fit(self, X, y):
        N, D = X.shape

        count = np.bincount(y, minlength=2)

        y_mode = np.argmax(count)

        self.splitSatisfied = y_mode
        self.splitNSatisfied = None
        self.splitVariable = None
        self.splitValue = None

        if np.unique(count).size <= 1:
            return

        y_base = count / len(y)
        baseEntropy = entropy(y_base)
        maxInfoGain = 0

        for d in range(D):
            for n in range(N):
                value = X[n, d]

                y_sat = mode(y[X[:, d] > value])
                y_not = mode(y[X[:, d] <= value])

                y_pred = y_sat * np.ones(N)
                y_pred[X[:, d] <= value] = y_not

                # To ignore the error given when trying to divide empty array
                np.seterr(divide='ignore', invalid='ignore')
                n_yes = y[X[:, d] > value]
                y_yes_count = np.bincount(n_yes, minlength=2)
                y_yes_count = y_yes_count / len(n_yes)

                n_not = y[X[:, d] <= value]
                y_not_count = np.bincount(n_not, minlength=2)
                y_not_count = y_not_count / len(n_not)

                infoGain = baseEntropy - (len(n_yes) / len(y)) * entropy(y_yes_count) - (len(n_not) / len(y)) * entropy(
                    y_not_count)

                if maxInfoGain < infoGain:
                    maxInfoGain = infoGain
                    self.splitVariable = d
                    self.splitValue = value
                    self.splitSatisfied = y_sat
                    self.splitNSatisfied = y_not


def entropy(p):
    plogp = 0 * p
    plogp[p > 0] = p[p > 0] * np.log(p[p > 0])
    return -np.sum(plogp)
