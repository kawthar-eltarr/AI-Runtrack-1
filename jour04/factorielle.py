# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:18:45 2020

@author: straw
"""
def factor(k):
    if k == 0:
        f = 1
    else:
        f = k*factor(k-1)
    return f

factor(6)
