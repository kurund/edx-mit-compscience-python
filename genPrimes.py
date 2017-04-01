#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 01:04:03 2017

@author: kurund
"""

def genPrimes():
    num = 2
    prime_numbers = []

    while True:
        prime_numbers.append(num)
        yield num
        isPrime = False
        while not isPrime:
            num += 1
            for i in prime_numbers:
                if num % i == 0:
                    break
            else:
                isPrime = True