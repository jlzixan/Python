import numpy as np


def test_run():
    #Masking
    b = np.random.randint(0,50, size =[4,4])
    print(b, "\n")

    
    mean = b.mean() #print elements that are less than the mean
    print(b[b<mean])

    print(mean)

    b[b<mean] = mean #replace the int that is less than mean with mean
    print(b)

if __name__ == "__main__":
    test_run()
    
