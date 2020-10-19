# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:42:16 2020

@author: straw
"""
import numpy as np
import random

def checkerboard(n):
    board = np.zeros((n,n))
    
    #p = random.randint(0, n-1)
    #board[0, p] = board[0, p] + 1
    
    for i in range(0, n):
        for j in range(0, n):
            print()
            #board[i, p] = board[i, p] + 1    
    return board

checkerboard(10)


