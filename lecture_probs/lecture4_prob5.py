def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    result = min(max(x,lo),hi)
    return result
    
    #if max(x,lo)==lo:
    #    return lo
    #elif min(x,hi)==hi:
    #    return hi
    #else:
    #    return x
