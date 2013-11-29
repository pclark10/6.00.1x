def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    a=0
    b=0
    c=0
    while 6*a < n:
        if 6*a + 9*b + 20*c == n:
            return True
        while 6*a + 9*b <= n:
            if 6*a + 9*b + 20*c == n:
                return True
            while 6*a + 9*b + 20*c <= n:
                if 6*a + 9*b + 20*c == n:
                    return True
                c+=1
            c=0
            b+=1
        b=0
        a+=1
    else:
        return False