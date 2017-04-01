#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:45:16 2017

@author: kurund
"""

#find the number of type word 'bob' occurs in the given string
s = 'ovlzobooobhobooubbob'
count = 0
index = 0
for i in s: 
    if i == 'b' and index < len(s) -2 :
        if s[index+1] == 'o' and s[index+2] == 'b':
            count += 1        
    index += 1

print("Number of times bob occurs is:" + str(count))