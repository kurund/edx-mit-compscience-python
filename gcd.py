#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 21:47:13 2017

@author: kurund
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if a == b:
        return a
    elif a < b:
        start = a
    elif b < a:
        start = b
            
    while start > 0:
        if start == 1:
            return 1
        elif a%start == 0 and b%start == 0:
            return start
        start -= 1
    
    
#print(gcdIter(2,12))
#print(gcdIter(6,12))
#print(gcdIter(9,12))
#print(gcdIter(17,12))


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == b or b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
        
print(gcdRecur(2,12))
print(gcdRecur(6,12))
print(gcdRecur(9,12))
print(gcdRecur(17,12))
        
