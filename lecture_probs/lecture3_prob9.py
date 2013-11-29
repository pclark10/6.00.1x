low=0
high=100
guess=(high+low)/2
ans=''
corr_ans='hlc'

print('Please think of a number between 0 and 100!')

while ans != 'c':
    print 'Is your secret number',guess,'?'
    ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly. ")
    if ans=='l':
        low=guess
    if ans=='h':
        high=guess
    if ans not in corr_ans:
        print 'Sorry, I did not understand your input.'
    guess=(high+low)/2
    
    
print 'Game over. Your secret number was:', guess