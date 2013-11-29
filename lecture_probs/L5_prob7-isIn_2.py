def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid=len(aStr)/2
    midc=aStr[mid]
    print('mid=',mid,'midc=',midc)
    while mid > 0:
        if char==midc:
            return 'True'
        elif char < midc:
            aStr=aStr[0:mid]
        else:
            aStr=aStr[mid:-1]
    return isIn(char,aStr)