"""Using time function"""
import time
#capture snapshot of functions


def test_run():
    t1 = time.time()
    print("ML4T")
    t2 = time.time()
    print("Time taken by pritn statement is ", t2 - t1, " seconds")



if __name__ == "__main__":
    test_run()
