import numpy as np
import random 
import math
import sys

# This is a single line comment, which starts with `#`in python
# Task:
# Make the following function execute faster/more efficiently.
# make use of numpy as you deem fit.

def convert_to_polar(N):
    """
    Generate a random set of N (x,y) cartesian coordinates, 
    convert them to polar coordinates.
    Hints
    tuple (a,b) in python is  a sequence of immutable data.     
    """
    cartesian_set = []
    a = 0
    while  a < N :
        cartesian_set.append(   tuple (random.sample(range(1, 100), 2) ) )
        a+=1 
    polar_set = []
    index = 0
    for coordinate in cartesian_set:
        x,y = coordinate # coordinate is a tuple, we can split it to x, y
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(float(y), x)
        polar_set.append (  tuple([r,theta]))

    return polar_set

if __name__ == "__main__":
    N = sys.argv[1]
    convert_to_polar(int (N) )
