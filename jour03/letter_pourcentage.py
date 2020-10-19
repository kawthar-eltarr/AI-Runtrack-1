# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:20:27 2020

@author: straw
"""
import string
import pandas as pd
import matplotlib.pyplot as plt

alphabet = list(string.ascii_lowercase)

file = open("data.txt", "r")
content = file.read()
file.close()
content = content.lower()

# convert input to list of chars so it is easy to get into pandas 
content_list = list(content)

# create a dataframe where each char is one row
df = pd.DataFrame({'Alphabet': content_list})

df = df[df['Alphabet'].isin(alphabet)].reset_index(drop=True)

df = df['Alphabet'].value_counts(normalize=True)

plt.bar(df.index, df, width=0.5, color='g')
plt.show()

