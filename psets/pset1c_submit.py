s='abc'

test=''
test2=''
prev_ltr=''

for ltr in s:
    if ltr >= prev_ltr:
        test += ltr
        prev_ltr = ltr
    else:
        if len(test) > len(test2):
            test2 = test
        prev_ltr=ltr
        test=ltr
if test2 == '':
    test2=test
print 'Longest substring in alphabetical order is:', test2