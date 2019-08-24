import numpy as np
from scipy import stats

def euclidean_dist_squared(X, Xtest):
    """Computes the Euclidean distance between rows of 'X' and rows of 'Xtest'

    Parameters
    ----------
    X : an N by D numpy array
    Xtest: an T by D numpy array

    Returns: an array of size N by T containing the pairwise squared Euclidean distances.

    Python/Numpy (and other numerical languages like Matlab and R)
    can be slow at executing operations in `for' loops, but allows extremely-fast
    hardware-dependent vector and matrix operations. By taking advantage of SIMD registers and
    multiple cores (and faster matrix-multiplication algorithms), vector and matrix operations in
    Numpy will often be several times faster than if you implemented them yourself in a fast
    language like C. The following code will form a matrix containing the squared Euclidean
    distances between all training and test points. If the output is stored in D, then
    element D[i,j] gives the squared Euclidean distance between training point
    i and testing point j. It exploits the identity (a-b)^2 = a^2 + b^2 - 2ab.
    The right-hand-side of the above is more amenable to vector/matrix operations.
    """

    return np.sum(X**2, axis=1)[:,None] + np.sum(Xtest**2, axis=1)[None] - 2 * np.dot(X,Xtest.T)

    # without broadcasting:
    # n,d = X.shape
    # t,d = Xtest.shape
    # D = X**2@np.ones((d,t)) + np.ones((n,d))@(Xtest.T)**2 - 2*X@Xtest.T

class KNN:

    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X = X # just memorize the trianing data
        self.y = y 

    def predict(self, Xtest):
        # X = self.X
        # y = self.y
        # N, t = X.shape
        # k = self.k
        #
        # result = utils.euclidean_dist_squared(X, Xtest)
        #
        # y_pred = np.zeros(t)
        #
        # for i in range(t):
        #     #sort the individual and grab the k elements determine the mode
        #     temp_X = result[:,i]
        #     sorted_arg = np.argsort(temp_X)
        #
        #     neighbours = sorted_arg[:k]
        #     neighbours = y[neighbours]
        #     label = stats.mode(neighbours)
        #     label = label[0]
        #     y_pred[i] = label[0]
        #
        # return y_pred

        X = self.X
        y = self.y
        k = self.k

        result = utils.euclidean_dist_squared(X, Xtest)
        N,t = result.shape
        y_pred = np.zeros(t)

        for i in range(t):
            temp_X = result[:,i]
            sorted_arg = np.argsort(temp_X)   #Sort based on arguments

            neighbours = sorted_arg[:k]
            neighbours = y[neighbours]
            label = stats.mode(neighbours)
            label = label[0]
            y_pred[i] = label[0]

        return y_pred