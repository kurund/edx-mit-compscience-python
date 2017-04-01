#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:43:47 2017

@author: kurund
"""


def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exponent = 0
    while base**exponent <= round(num):
        exponent +=1
        
    actual =  base**exponent
    actualMinus = base**(exponent-1)
    
    a = round(abs(actual - num))
    b = round(abs(actualMinus - num))

    if a < b:
        return exponent
    else:
        return exponent - 1

    
print(closest_power(3,12)) # 2
print(closest_power(4,12)) # 2
print(closest_power(4,1)) # 0
print(closest_power(10, 550.0)) #2
print(closest_power(15, 8.0)) #0