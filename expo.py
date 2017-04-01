#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 20:44:00 2017

@author: kurund
"""
    
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    i = 0
    itpower = 1
    while i <= exp-1:
        itpower = itpower * base
        i +=1
    return itpower

#print(iterPower(2, 3))    
#print(iterPower(-8.96, 0))

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp - 1)
        
#print(recurPower(2,3))