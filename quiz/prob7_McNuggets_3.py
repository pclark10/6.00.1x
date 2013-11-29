def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    a=0
    b=0
    c=0
    result=0
    while 6*a < n:
        while 6*a + 9*b < n:
            while 6*a + 9*b + 20*c < n:
                if 6*a + 9*b + 20*c == n:
                    return True
                c+=1
            if 6*a + 9*b + 20*c == n:
                return True
            b+=1
        if 6*a + 9*b + 20*c == n:
            return True
        a+=1
        print a, b, c
    if 6*a + 9*b + 20*c == n:
        return True
    else:
        return False