def larger(a,b):
    """This returns the max of two values.

    >>>> find_max(5,8)"""

    if(a>b):
       print "a is greater than b"
    else:
       print "b is greater than a"

if __name__ == "__main__":                                                       
    import sys                                                                   
    larger(int(sys.argv[1]), int(sys.argv[2]))
