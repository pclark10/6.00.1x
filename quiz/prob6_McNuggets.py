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
    while result <= n:
        result = 6*a + 9*b + 20*c
        if result > n:
            return False
        elif result == n:
            return True
        else:
            a+=1
            ...