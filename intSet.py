#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:01:45 2017

@author: kurund
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    
    def intersect(self, s):
        c = intSet()
        for i in s.vals:
            if i in self.vals:
                c.insert(i)
        return '{' + ','.join([str(e) for e in c.vals]) + '}'

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def __len__(self):
        count = 0
        for i in self.vals:
            count += 1
        return count


"""    
    
setA = intSet()

setA.insert(1)

setA.insert(2)

setA.insert(3)

setB = intSet()

setB.insert(2)

setB.insert(3)

setB.insert(4)

print(setA.intersect(setB))

"""