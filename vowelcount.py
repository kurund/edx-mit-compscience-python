#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:14:17 2017

@author: kurund
"""

#find the number of vowels in the given string
s = 'azcbobobegghakl'
vowel_count = 0
for i in s: 
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowel_count += 1

print("Number of vowels:" + str(vowel_count))