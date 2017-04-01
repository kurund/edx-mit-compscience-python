#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 00:19:28 2017

@author: kurund
"""

#balance = 42
balance = 3926
balance = 4773
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


def calculateMinimumMonthlyPayment(balance, minimumMonthlyPayment=10):
    payment = calculateCCBalance(balance, 1, minimumMonthlyPayment)
    
    if payment / minimumMonthlyPayment*12 <= 0:
        return round(minimumMonthlyPayment, 2)
    else:
        return calculateMinimumMonthlyPayment(balance, minimumMonthlyPayment +10 )
    

print('Lowest Payment: ' + str(calculateMinimumMonthlyPayment(balance, 10)))
