# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:42:16 2020

@author: straw
"""
import numpy as np
import random

def checkerboard(n):
    board = np.zeros((n,n))
    
    p = random.randint(0, n-1)
    board[0, p] = board[0, p] + 1
    restricted_columns = [p]
    for i in range(1, n):
        emplacements = []
        for j in range(0, n):
            if (j < n - 1) and (j !=0):
                if (board[i-1, j-1]!=1) and (board[i-1, j]!=1) and (board[i-1, j+1]!=1) and (j not in restricted_columns):
                    emplacements.append(j)
            elif (j==n-1):
                if (board[i-1, j-1]!=1) and (board[i-1, j]!=1) and (j not in restricted_columns):
                    emplacements.append(j)
            elif (j==0):
                if (board[i-1, j]!=1) and (board[i-1, j+1]!=1) and (j not in restricted_columns):
                    emplacements.append(j)
        x = random.choice(emplacements)
        restricted_columns.append(x)
        board[i, x] = board[i, x] + 1
        
    board = np.where(board==0, 'X', board)
    board = np.where(board=='1.0', 'O', board)
    print(board)
    return board

board = checkerboard(8)



