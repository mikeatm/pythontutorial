import numpy as np
import math
import random 
import sys

def fill_list(N):
    """
    generate a list of  points obtained from N 
    consecutive values,  satisfying f(x) :  1/sqrt(2*pi) exp( -(x^2)/2 ) 
    """
    x = [ float(i)/N  for i in range(N) ] 
    y = []
    for i in range(N) :
        y.append(  math.exp(-x[i])*x[i] ) 


if __name__ == "__main__":
    N = int( sys.argv[1]) 
    fill_list(N) 
