"""Array attributes"""

import numpy as np

def test_run():

    a = np.random.random((5,4))
    print(a.shape) # print nxn array dimension
    print(len(a.shape)) #print dimension of array
    print(a.shape[0]) #number of rows
    print(a.shape[1]) #number of columns

    print(a.size) #number of elements in array

    print(a.dtype) #type of elements

if __name__ == "__main__":
    test_run()
