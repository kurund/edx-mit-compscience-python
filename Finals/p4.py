#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 22:26:20 2017

@author: kurund
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    # build increaing list
    increasingList = {}
    
    icounter = 0
    ecount = 0
    for i in L:
        if ecount == 0:
            increasingList[icounter] = []
            increasingList[icounter].append(i)
        elif L[ecount] >= L[ecount-1]:
            increasingList[icounter].append(i)
        else:
            icounter += 1
            increasingList[icounter] = []
            increasingList[icounter].append(i)
        
        ecount += 1
    
    # find the longest run
    iLongRun = longestRun(increasingList)
    
    # build decreaing list
    decreasingList = {}
    
    dcounter = 0
    ecount = 0
    for i in L:
        if ecount == 0:
            decreasingList[dcounter] = []
            decreasingList[dcounter].append(i)
        elif L[ecount] <= L[ecount-1]:
            decreasingList[dcounter].append(i)
        else:
            dcounter += 1
            decreasingList[dcounter] = []
            decreasingList[dcounter].append(i)
        
        ecount += 1    

    # find the longest run
    dLongRun = longestRun(decreasingList)

    # check which one is the longest run
    longest = iLongRun
    if len(iLongRun) < len(dLongRun):
        longest = dLongRun
    # check which occurs first
    elif len(iLongRun) == len(dLongRun):
        for iIndex in iLongRun:
            iIndex = iIndex
        
        for dIndex in dLongRun:
            dIndex = dIndex

        if dIndex < iIndex:
            longest = dLongRun

    # calculate the sum
    longestRunSum = 0
    for i in longest:
        for j in longest[i]:
            longestRunSum = longestRunSum + j
    
    return longestRunSum
    

def longestRun(L):
    lRun = []
    for i in L:
        if not lRun or len(L[i]) > len(lRun):
            lRun = {i: L[i]}
        
    return lRun

L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
print(longest_run(L))

L = [5, 4, 10]
print(longest_run(L))