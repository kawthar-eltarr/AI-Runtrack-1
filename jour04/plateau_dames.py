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
    board[0, 4] = board[0, 4] + 1
    print(board)
    for i in range(1, n):
        for j in range(0, n):
            print('Ligne {}, colonne {}'.format(i,j))
            if (j < n - 1) and (j !=0):
                if (board[i-1, j-1]!=1) and (board[i-1, j]!=1) and (board[i-1, j+1]!=1):
                    print("Emplacement de dame possible")
                    print()
                    #board[i, p] = board[i, p] + 1   
            elif (j==n-1):
                if (board[i-1, j-1]!=1) and (board[i-1, j]!=1):
                    print("Emplacement de dame possible")
                    print()
            elif (j==0):
                if (board[i-1, j]!=1) and (board[i-1, j+1]!=1):
                    print("Emplacement de dame possible")
                    print()
    return board

checkerboard(8)


