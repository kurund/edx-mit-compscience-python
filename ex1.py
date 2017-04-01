#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 16:48:00 2017

@author: kurund
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
"""
def minusone(L):
    L = L + 1    
    return L
    

testList = [1, -4, 8, -9]
    
applyToEach(testList, minusone)
#  [2, -3, 9, -8]
print(testList)

"""

testList = [1, -4, 8, -9]

def square(L):
    L = L * L
    return L
    

applyToEach(testList, square)

#[1, 16, 64, 81]
print(testList)