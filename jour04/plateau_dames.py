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
        emplacements = []
        for j in range(0, n):
            print('Ligne {}, colonne {}'.format(i,j))
            if (j < n - 1) and (j !=0):
                if (board[i-1, j-1]!=1) and (board[i-1, j]!=1) and (board[i-1, j+1]!=1):
                    #print("Emplacement de dame possible")
                    emplacements.append(j)
                    #print()
            elif (j==n-1):
                if (board[i-1, j-1]!=1) and (board[i-1, j]!=1):
                    #print("Emplacement de dame possible")
                    emplacements.append(j)
                    #print()
            elif (j==0):
                if (board[i-1, j]!=1) and (board[i-1, j+1]!=1):
                    #print("Emplacement de dame possible")
                    emplacements.append(j)
                    #print()
        print(emplacements)
        x = random.choice(emplacements)
        print(x)
        print()
        board[i, x] = board[i, x] + 1
    return board

board = checkerboard(8)



