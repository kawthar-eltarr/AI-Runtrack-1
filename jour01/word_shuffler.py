# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:40:35 2020

@author: straw
"""
import string

def word_shuffler():
    # User word
    given_chr = str(input("Please enter a word: "))
    given_chr = given_chr.lower()
    
    for c in given_chr:
        if c not in string.ascii_lowercase:
            raise ValueError('Seulement les lettres miniscules sont acceptés.')
    
    given_chr = list(given_chr)
    
    last_chr = given_chr[len(given_chr)-1]
    
    for i in range(len(given_chr)-1, -1, -1):
        if given_chr[i] < last_chr:
            pivot = given_chr[i]
            break
    
    index_pivot = given_chr.index(pivot)
    
    given_chr[index_pivot] = last_chr
    
    given_chr[len(given_chr)-1] = pivot
    
    given_chr[index_pivot+1:len(given_chr)] = sorted(given_chr[index_pivot+1:len(given_chr)])
    
    print(given_chr)
    
    return given_chr

word_shuffler()
