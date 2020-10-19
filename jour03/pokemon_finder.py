# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:28:16 2020

@author: straw
"""
import os
import re
import numpy as np
import pandas as pd

# Define path
os.chdir(r'C:\Users\straw\Desktop\AIS\RunTrack1\Day3')

file = open("data.txt", "r")
content = file.read()
file.close()

pokemon = pd.read_csv('Pokemon-database.csv', sep=',', encoding = "ISO-8859-1")

pokemon_list = np.unique(pokemon['Pokemon Name'])

for p in pokemon_list:
    if p in content:
        print('Le pokemon est là.')
        print(p)
        
