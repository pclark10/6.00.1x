vowels='aeiou'
numVowels=0
for letter in s:
    if letter in vowels:
        numVowels += 1
print('Number of vowels: ', numVowels)