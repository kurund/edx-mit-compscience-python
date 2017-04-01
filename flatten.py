#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 21:11:44 2017

@author: kurund
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flatList = []
    for i in aList:
        if type(i) == list:
            flatList.extend(flatten(i))
        else:
            flatList.append(i)
    return flatList

    
L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(L))
# [1,'a','cat',2,3,'dog',4,5]
