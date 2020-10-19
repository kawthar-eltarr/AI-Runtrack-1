# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:43:55 2020

@author: straw
"""
import re
import pandas as pd
import matplotlib.pyplot as plt

file = open("data.txt", "r")
content = file.read()
file.close()
content = content.lower()

res = re.findall(r"\w+", content)

lengths = [len(r) for r in res]

df = pd.DataFrame({'Tailles': lengths})

df = df['Tailles'].value_counts(normalize=True)

plt.bar(df.index, df, width=0.5, color='g')
plt.show()


