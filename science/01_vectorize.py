import numpy as np
import math
import random 
import sys
import time

def fill_list(N):
    """
    generate a list of  points obtained from N 
    consecutive values,  satisfying f(x) :  1/sqrt(2*pi) exp( -(x^2)/2 ) 
    """
    x = [ float(i)/N  for i in range(N) ] 
    y = []
    for i in range(N) :
        y.append(  math.exp(-x[i])*x[i] ) 


def fill_list_np(N):
    """
    generate a list of  points obtained from N 
    consecutive values,  satisfying f(x) :  1/sqrt(2*pi) exp( -(x^2)/2 ) 
    """
    x = np.arange(N, dtype='d') / N
    y = np.exp(x)


if __name__ == "__main__":
    N = int(sys.argv[1]) 
    start = time.time()    
    fill_list(N) 
    end = time.time()
    print 'Time taken for pure python: %s' % (end - start)

    start = time.time()    
    fill_list_np(N) 
    end = time.time()

    print 'Time taken for numpy: %s' % (end - start)
