def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    result=()
    x=0
    while x < len(aTup):
        print x
        if x%2==0:
            result += (aTup[x],)
        x+=1
    return result