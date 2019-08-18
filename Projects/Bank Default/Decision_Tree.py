import numpy as np
from Decision_Stump import DecisionStumpErrorRate


class DecisionTree:

    def __init__(self, max_depth, stump_class=DecisionStumpErrorRate):
        self.max_depth = max_depth
        self.stump_class = stump_class

    def fit(self, X, y):
        N, D = X.shape

        # Learn a decision stump
        splitModel = self.stump_class()
        splitModel.fit(X, y)

        if self.max_depth <= 1 or splitModel.splitVariable is None:
            # If we have reached the maximum depth or the decision stump does
            # nothing, use the decision stump

            self.splitModel = splitModel
            self.subModel1 = None
            self.subModel0 = None
            return

        # Determines the splitting criteria and conditions
        j = splitModel.splitVariable
        value = splitModel.splitValue

        # Splitting whole array into partions that satisfy the condition
        splitIndex1 = X[:, j] > value
        splitIndex0 = X[:, j] <= value

        # Fit model to each split
        self.splitModel = splitModel  # Assigns to memory the model that is being used
        self.subModel1 = DecisionTree(self.max_depth - 1, stump_class=self.stump_class)
        self.subModel1.fit(X[splitIndex1], y[splitIndex1])
        self.subModel0 = DecisionTree(self.max_depth - 1, stump_class=self.stump_class)
        self.subModel0.fit(X[splitIndex0], y[splitIndex0])

    def predict(self, X):
        M, D = X.shape
        y = np.zeros(M)

        # Get values from model
        splitVariable = self.splitModel.splitVariable
        splitValue = self.splitModel.splitValue
        splitSatisfied = self.splitModel.splitSatisfied

        if splitVariable is None:
            # If no further splitting, return the majority label
            y = splitSatisfied * np.ones(M)

        elif self.subModel1 is None:
            # the case with depth = 1, just a single stump
            return self.splitModel.predict(X)

        else:
            # Recuse on both sub-models
            j = splitVariable
            value = splitValue

            splitIndex1 = X[:, j] > value
            splitIndex0 = X[:, j] <= value

            y[splitIndex1] = self.subModel1.predict(X[splitIndex1])
            y[splitIndex0] = self.subModel0.predict(X[splitIndex0])

        return y
