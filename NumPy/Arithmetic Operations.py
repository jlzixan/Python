"""Arithmetic Operations"""
import numpy as np

def test_run():
    a = np.array([(1,2,3,4,5),(10,20,30,40,50)])
    print("OG array a:\n",a)

    #Multiply a by 2
    print("\nMultiply a by 2:\n", 2*a)
    
    #Divide a by 2
    print("\nDivide a by 2:\n", a/2)

    b = np.array([(100,200,300,400,500),(1,2,3,4,5)])
    print("OG array b:\n",b)

    #Add two arrays
    print("\nAdd a+b:\n", a+b)

    #Multiply two arrays
    'note: it is not linear multiplication, it is element time respective element in second array'
    print("\nMultiplcation a*b:\n",a*b)
    #Instead use np.dot(a,b)
    print("\nDot Product a.b:\n",np.dot(np.array([(1,0),(0,1)]),np.array([(4,1),(2,2)])))

if __name__ == "__main__":
    test_run()
