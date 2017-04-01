#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 18:40:50 2017

@author: kurund
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    counter = 1
    nTup = ()
    for i in aTup:
        if counter%2 != 0:
            nTup += (i,)
        counter +=1
    return nTup

print(oddTuples((1,2,3,4)))