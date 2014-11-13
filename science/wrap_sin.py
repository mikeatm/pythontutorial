import ctypes

# the standard c math library
libm = ctypes.cdll.LoadLibrary('libm.so')
# You can specify the data types of the function call
libm.sin.argtypes = [ctypes.c_double]
libm.sin.restype = ctypes.c_double

def wrapsin(*args):
    """Wrapper around the std lib math library.

    >>> wrapsin(1.0,1.6,0.5,0.3454)"""
    ret=[]
    for num in args:
        ret.append( libm.sin(float(num)) )
    return ret
    
