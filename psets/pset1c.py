s='gtmwmicfajidruhsffyfhqq' #do not include in pset submission

test=''
test2=''
prev_ltr=''

for ltr in s:
    print "the current letter is", ltr
    if ltr >= prev_ltr:
        test += ltr
        prev_ltr = ltr
    else:
	print "current test:",test
	print "current test2:",test2
        if len(test) > len(test2):
            print "len",test,">","len",test2
            test2 = test
        prev_ltr=ltr
        test=ltr
if test2 == '':
    test2=test
if len(test) > len(test2):
    test2=test
print "current test:",test
print "current test2:",test2
print 'Longest substring in alphabetical order is:', test2