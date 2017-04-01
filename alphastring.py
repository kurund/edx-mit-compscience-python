#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:11:19 2017

@author: kurund
"""

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.

#s = 'abcdefghijklmnopqrstuvwxyz'
s = 'zyxwvutsrqponmlkjihgfedcba'

# build a list of string in which letters occur in alpha order
index = 0;
#initialize empty string to build the 
string = ''
# list to store all alpha strings
alphalist = []
for i in s:
    if index == 0:
        string = i
    elif i >= s[index-1]:
        string = string + i
        alphalist.append(string)
    else:
        alphalist.append(string)
        string = i
    index += 1

    
print(alphalist)    
# loop through built list and print the longest
longeststring = alphalist[0]
sindex = 0
for j in alphalist:
    if sindex > 0 and len(j) > len(longeststring):    
        longeststring = j
    sindex += 1        
print('Longest substring in alphabetical order is: ' + longeststring)