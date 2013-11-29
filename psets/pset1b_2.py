s='azcbobobegghakl' #do not include in pset submission

bob='bob'
numBobs=0
count=0

for letter in s:
    if letter=='b':
        if bob == s[count:(count+len(bob))]:
            numBobs += 1
    count +=1
print('Number of times bob occurs is: ', numBobs)