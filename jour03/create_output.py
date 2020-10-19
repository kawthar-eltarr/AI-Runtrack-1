# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:09:08 2020

@author: straw
"""
entry = input("Please enter the desired content :")
file = open("output.txt", "w")
file.write(entry)
file.close()

