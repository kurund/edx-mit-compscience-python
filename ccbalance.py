#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 23:42:09 2017

@author: kurund
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def calculateCCBalance(balance, duration = 1):
    '''
    balance int or float
    duration int
    return balance amount
    '''

    '''
    Monthly interest rate= (Annual interest rate) / 12.0
    Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    '''
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    updateBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    #print ('Month ' + str(duration) + " : " + str(updateBalanceEachMonth))
    if duration == 12:
        return round(updateBalanceEachMonth, 2)
    else:
        return calculateCCBalance(updateBalanceEachMonth, duration + 1)
    
print('Remaining balance: ' + str(calculateCCBalance(balance)))
        
        
#print('Remaining balance: ' + str(calculateCCBalance(balance))
#Remaining balance: 31.38
