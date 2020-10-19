# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:48:49 2020

@author: straw
"""
import os
import re
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\straw\Desktop\AIS\RunTrack1\Day3')

file = open("data.txt", "r")
content = file.read()
file.close()
content = content.lower()

res = re.findall(r"\w+", content)
    
first_letters = [w[0] for w in res]

df = pd.DataFrame({'Occurence': first_letters})

df = df['Occurence'].value_counts(normalize=True)

plt.bar(df.index, df, width=0.5, color='g')
plt.show()

