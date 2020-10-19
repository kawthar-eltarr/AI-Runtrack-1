# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:28:12 2020

@author: straw
"""
def power(x, p):
    if p == 1:
        res = x
    if (p>1):
        res = x*power(x, p-1)
    return res

power(2, 2)
