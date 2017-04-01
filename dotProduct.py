#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:24:53 2017

@author: kurund
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    dotProduct = 0
    
    for i in range(0, len(listA)):
        dotProduct += listA[i]*listB[i]
    
    return dotProduct
    
    
listA = [1, 2, 3]
listB = [4, 5, 6]
 
print(dotProduct(listA, listB))