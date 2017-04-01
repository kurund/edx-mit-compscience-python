#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 17:38:59 2017

@author: kurund
"""

print('Please think of a number between 0 and 100!')
start = 0
end = 100

ans = ''
while ans != 'c':
    snumber = int((start + end)/2)
    print('Is your secret number ' + str(snumber) + '?')
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if ans == 'c':
        print('Game over. Your secret number was: ' + str(snumber))
    elif ans == 'l':
        start = snumber
    elif ans == 'h':
        end = snumber
    else:
        print('Sorry, I did not understand your input.')
    