def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr=='':
        return False
    mid=len(aStr)/2
    midchr=aStr[mid]
    print(char,aStr,mid,midchr)
    if mid==0:
        return False
    elif char==midchr or char==aStr:
        return True
    elif char<midchr:
        return isIn(char,aStr[0:mid])
    elif char>midchr:
        return isIn(char,aStr[mid:])
    #else:
    #    return False