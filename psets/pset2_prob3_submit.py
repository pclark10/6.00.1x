month=0
monthlyUnpaidBalance=0
updatedBalance=balance
monthlyInterestRate=annualInterestRate/12.0
lowerBound=balance/12
upperBound=(balance*(1+monthlyInterestRate)**12)/12.0
guess=0
epsilon=0.01

while abs(updatedBalance) >= epsilon:
    guess=(lowerBound+upperBound)/2
    updatedBalance=balance
    for month in range(1,13):
        monthlyUnpaidBalance = updatedBalance-guess
        updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
    if monthlyUnpaidBalance < 0:
        upperBound=guess
    else:
        lowerBound=guess

print 'Lowest Payment:',round(guess,2)