s='azcbobobegghakl' #do not include

bob='bob'
numBobs=0
count=0

while count < len(s):
    if bob[0] == s[count]:
        if bob == s[count:len(bob)]:
            numBobs += 1
    count +=1
print('Number of times bob occurs is: ', numBobs)

#for letter in s:
#    if letter==bob[0]
#    if bob in s:
#        numBobs += 1
#        numBobs
#print('Number of times bob occurs is: ', numBobs)