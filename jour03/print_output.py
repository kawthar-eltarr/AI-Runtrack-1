# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:17:10 2020

@author: straw
"""

file = open("output.txt", "r")
content = file.read()
file.close()
print(content)