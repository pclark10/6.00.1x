def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    result=0
    power=0
    while result < x:
        power += 1
        result = b**power
        if result > x:
            return power-1
    return power