monthlyPayment=0
monthlyUnpaidBalance=0
updatedBalance=0
monthlyInterestRate=annualInterestRate/12.0
amtPaid=0

for month in range(1,13):
    monthlyPayment=monthlyPaymentRate*balance
    monthlyUnpaidBalance = balance-monthlyPayment
    updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
    print 'Month:',month
    print 'Minimum monthly payment:',round(monthlyPayment, 2)
    print 'Remaining balance:', round(updatedBalance, 2)
    balance = updatedBalance
    amtPaid += monthlyPayment

print 'Total paid:',round(amtPaid,2)
print 'Remaining balance:', round(updatedBalance, 2)