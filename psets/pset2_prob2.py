monthlyPayment=0
monthlyUnpaidBalance=0
updatedBalance=balance
monthlyInterestRate=annualInterestRate/12.0
month=0

while updatedBalance > 0:
    updatedBalance=balance
    monthlyPayment += 10
    for month in range(1,13):
        monthlyUnpaidBalance = updatedBalance-monthlyPayment
        updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
        if updatedBalance <= 0:
            break

print 'Lowest Payment:',monthlyPayment
