import time

cnt1=0
cnt2=0

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    global cnt1
    cnt1+=1
    if exp==0:
        return 1
    if exp==1:
        return base
    else:
        if exp%2 != 0:
            return base * recurPowerNew(base, exp-1)
        else:
            return recurPowerNew(base*base, exp/2)
            
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
    global cnt2
    cnt2+=1
    if exp==0:
        return 1
    if exp==1:
        return base
    else:
        return base * recurPower(base, exp-1)

t0=time.clock()
recurPowerNew(32,900)
print cnt1
print time.time() - t0

t0=time.clock()
recurPower(32,900)
print cnt2
print time.time() - t0