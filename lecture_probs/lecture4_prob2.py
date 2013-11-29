def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)


b(3,2)

a(True, 3, 2)

####################################

if 3>2:
    if x:
        return y
    else:
        return z
else:
    if q>r:
        return q
    else:
        return r

#####################################

b(a, b)

return a(b>a, a, b)
if b>a:
    if x:
        return y
    else:
        return z
else:
    if q>r:
        return q
    else:
        return r