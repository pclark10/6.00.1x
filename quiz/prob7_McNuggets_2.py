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
    for var in [a, b, c]:
        var+=1
        result = 6*a +9*b + 20*c
        print var
        print result
        print a, b, c
        if result >= n:
            break