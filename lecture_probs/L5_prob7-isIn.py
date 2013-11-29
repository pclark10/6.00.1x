def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid=len(aStr)/2
    midc=aStr[mid]
    def biSrch(aStr):
        print('mid=',mid,'midc=',midc)
        if char==midc:
            return 'True'
        elif char < midc:
            return biSrch(aStr[0:mid])
        else:
            return biSrch(aStr[mid:-1])
    
    return biSrch(aStr)
