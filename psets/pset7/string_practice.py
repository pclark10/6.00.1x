import string
str1 = "Soft's the new pink!"
str2 = ' '
for i in str1:
    if i in string.punctuation:
        str2 += ' '
    else:
        str2 += i
print str2
str2 = str2.split(' ')
print str2