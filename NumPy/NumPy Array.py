"""Creating NumPy arrays"""
import numpy as np

def test_run():
    #Create 1D array
    #print(np.array([2,3,4]))

    #List of tuples to 2D array
    print(np.array([(2,3,4),(5,6,7)]))

    print("Empty Array")
    #Create empty 1D array
    print(np.empty(5))
    #Create empty 2D array
    print(np.empty((5,4)))
    
    print("Fill array with one")
    print(np.ones((5,4)))
    print("Change type")
    print(np.ones((5,4), dtype = np.int_)) #change from float to int
    
    #Create empty 3D array
    #print(np.empty((5,4,3)))

if __name__ == "__main__":
    test_run()
