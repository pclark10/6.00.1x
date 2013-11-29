def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    s3=''
    count=0
    while count < len(s1)+len(s2):
        print s3
        s3 += s1[count]
        s3 += s2[count]
        count += 1
    return s3