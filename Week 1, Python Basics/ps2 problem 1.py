balance = 999999
rmbalance = balance
annualInterestRate = 0.18

def rmBalance(balance,pymt,annualInterestRate):
    count = 0
    balance1 = balance
    while count < 12:
        remainingBalance = balance1 - pymt
        balance1 = remainingBalance + remainingBalance*(annualInterestRate/12)
        count += 1
    return balance1

lowerPymt = rmbalance/12
upperPymt = (rmbalance*(1+annualInterestRate/12)**12)/12
avgPymt = (lowerPymt + upperPymt)/2

while rmBalance(balance,avgPymt,annualInterestRate)>0.01 or rmBalance(balance,avgPymt,annualInterestRate)<-0.01 :
    
    if rmBalance(rmbalance,avgPymt,annualInterestRate)> 0.01:
        lowerPymt = avgPymt
    elif rmBalance(rmbalance,avgPymt,annualInterestRate)< 0.01:
        upperPymt = avgPymt
        
    avgPymt = (lowerPymt + upperPymt)/2
    

print("Lowest Payment: ", round(avgPymt,2))


