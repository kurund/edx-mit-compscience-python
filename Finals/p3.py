#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 18:26:09 2017

@author: kurund
"""

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
          
    mandString = ''
    if len(us_num) == 1:
        return trans[us_num]
    
    count = 1      
    for i in us_num:
        if int(i) == 1 and count == 1:
            mandString = 'shi'
        elif int(i) >= 2 and count == 1:
            mandString = trans[i] + ' shi'
        else :
            if int(i) != 0:
                mandString = mandString + ' ' +trans[i]
                
        count += 1
        
    return mandString         
          

print(convert_to_mandarin('1'))  #will return yi
print(convert_to_mandarin('36')) #will return san shi liu
print(convert_to_mandarin('20')) #will return er shi
print(convert_to_mandarin('16')) #will return shi liu
print(convert_to_mandarin('11')) #will return shi yi