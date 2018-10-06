"""Accessing array elements"""
import numpy as np

def test_run():
	#s[0:3] up to item two
	#s.ix[0:3] up to three items
	
    a = np.random.rand(5,4)
    print("Array:\n", a)

    #Accessing element at pos (3,2)
    element = a[3,2]
    print(element)

    #Elements in defined range
    print(a[0,1:3])

    #Slicing
    #note: Slice n:m:t specifies a range that starts at n, and stops before m, steps of size t
    print(a[:,0:3:2]) #print every other one

    #Assigning array element
    a[0,0] = 1
    print("Modify (0,0):\n", a)

    a[0,:] = 2
    print("Modify first row:\n", a)


    #Assigning a list to a column in an array
    a[:, 3] = [1,2,3,4,5]
    print("Modify by list:\n",a)

    #Accessing using list of indices
    print("\n")
    b = np.random.rand(5)
    print(b)
    selection = np.array([1,1,2,3])
    print(b[selection])

    #Masking
    print("Masking:")
    b = np.random.randint(0,50, size =[4,4])
    print(b)
    mean = b.mean()
    print(b[b<mean])
    

if __name__ == "__main__":
    test_run()

#https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html
