## do not include these vars in submission###########
balance=320000
annualInterestRate=0.2
#####################################################
month=0
monthlyUnpaidBalance=0
updatedBalance=balance
monthlyInterestRate=annualInterestRate/12.0
lowerBound=balance/12
upperBound=(balance*(1+monthlyInterestRate)**12)/12.0
guess=0

while round(updatedBalance) < 1 and round(updatedBalance) > 1: #currently gets stuck in an infinite loop
    guess=(lowerBound+upperBound)/2
    updatedBalance=balance
    for month in range(1,13):
        monthlyUnpaidBalance = updatedBalance-guess
        updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
    # How do I tell if the guess is too high or low?
    print 'Balance:', updatedBalance
    if updatedBalance < 1:
        lowerBound=guess
    if updatedBalance > 1:
        upperBound=guess


print 'Lowest Payment:',monthlyPayment