#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 22:45:31 2017

@author: kurund
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    elif char == aStr:
        return True
    elif len(aStr) == 1:
        return False
        
    half = int(len(aStr)/2)
    
    if half < 0:
        return False
    elif char == aStr[half]:
        return True
    elif char < aStr[half]:
        return isIn(char, aStr[0:half])
    elif char > aStr[half]:
        return isIn(char, aStr[half:])

            
        
#print(isIn('a', 'halloo'))   
#print(isIn('e', 'bdvv'))     
#print(isIn('s', 'm'))      