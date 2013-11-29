def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd=min(a,b)
    while gcd >= 1:
        if a%gcd==0 and b%gcd==0:
            return gcd
        else:
            gcd -= 1