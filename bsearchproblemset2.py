#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 01:26:48 2017

@author: kurund
"""

#balance = 42
balance = 320000
balance = 999999
annualInterestRate = 0.2

def calculateCCBalance(balance, duration = 1, minimumMonthlyPayment=10):
    '''
    balance int or float
    duration int
    return balance amount
    '''

    '''
    Monthly interest rate= (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    '''
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    updateBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    #print ('Month ' + str(duration) + " : " + str(updateBalanceEachMonth) + " -" + str(minimumMonthlyPayment))
    if duration == 12:
        return round(updateBalanceEachMonth, 2)
    else:
        duration += 1
        return calculateCCBalance(updateBalanceEachMonth, duration, minimumMonthlyPayment)
    
#print('Remaining balance: ' + str(calculateCCBalance(balance)))


def calculateMinimumMonthlyPayment(balance, minimumMonthlyPayment=0):
    
    """
    Monthly payment lower bound = Balance / 12
    Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
    """
    if minimumMonthlyPayment == 0:
        lbound = balance / 12   
        monthlyInterestRate = annualInterestRate / 12.0
        hbound = (balance * ( 1+ monthlyInterestRate)**12)/12.0
    
        minimumMonthlyPayment = (lbound + hbound) / 2

    
    payment = calculateCCBalance(balance, 1, minimumMonthlyPayment)
    
    if payment / minimumMonthlyPayment*12 <= 0:
        return round(minimumMonthlyPayment, 2)
    else:
        
        return calculateMinimumMonthlyPayment(balance, minimumMonthlyPayment )

print('Lowest Payment: ' + str(calculateMinimumMonthlyPayment(balance)))

"""
#balance = 42
balance = 999999
annualInterestRate = 0.18

updatedBalance = balance
monthlyInterestRate = (annualInterestRate) / 12
epsilon = 0.01
numGuesses = 0
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12
ans = (upperBound + lowerBound)/2.0

while abs(0 - updatedBalance) >= epsilon:
    #print('low = ' + str(lowerBound) + ' high = ' + str(upperBound) + ' ans = ' + str(ans))
    updatedBalance = balance
    numGuesses += 1
    for i in range(0, 12):
        updatedBalance = round(((updatedBalance - ans) * (1 + monthlyInterestRate)), 2)
    if  updatedBalance >= 0:
        lowerBound = ans
    else:
        upperBound = ans
    ans = (upperBound + lowerBound)/2.0
#print('numGuesses = ' + str(numGuesses))
print("Lowest Payment: " + str(round(ans, 2)))
"""

