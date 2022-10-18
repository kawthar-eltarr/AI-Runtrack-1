# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:20:25 2020

@author: straw
"""
import os
import re
os.chdir(r'C:\Users\straw\Desktop\AIS\RunTrack1\Day3')

file = open("domains.xml", "r")
content = file.read()
file.close()
res = re.findall(r"\.[a-z]{2,4}[<|/|\n]", content)
res = [r.replace("<", "").strip() for r in res]
print('Nombre d\'extentions présentes dans le fichier : {}.'.format(len(res)))
print(res)
