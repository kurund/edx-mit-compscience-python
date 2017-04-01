#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:46:06 2017

@author: kurund
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    inter = {}
    diff = {}

    for i in d1:
        if i in d2:
           inter[i] = f(d1[i], d2[i])
        else:
           diff[i] = d1[i]
    
    for i in d2:
        if i in d1:
           inter[i] = f(d1[i], d2[i])
        else:
           diff[i] = d2[i]
    
    return (inter, diff)
    
def f(a,b):
    return a + b
    
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
print(dict_interdiff(d1, d2))  # ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})


def f(a,b):
    return a > b
    
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print(dict_interdiff(d1, d2))  # ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})