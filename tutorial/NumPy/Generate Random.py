"""Generating Random Numbers"""
import numpy as np

def test_run():
    #Generate an array full of random numbers, uniformly sampled from [0.0,1.0)
    print("Random Uniform Variables")
    print(np.random.random((5,4)))

    #Generate normal distribution
    print("Random Normal Variables")
    print(np.random.normal(size=(2,3))) #Array 2X3 array
    print(np.random.normal(50, 10, size=(2,3))) #mean = 50, sd = 10

    #Generate random integers
    print("Random Integers")
    print(np.random.randint(10)) # a single int in [0,10)
    print(np.random.randint(0,10)) #same as above but explicity
    print(np.random.randint(0,10,size=5)) #5 random int as 1D array
    print(np.random.randint(0,10,size=(2,3))) #2X3 array of random int


if __name__ == "__main__":
    test_run()
          
