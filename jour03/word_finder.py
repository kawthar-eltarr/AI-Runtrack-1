# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:41:48 2020

@author: straw
"""
import re

file = open("data.txt", "r")
content = file.read()
file.close()
res = re.findall(r"\w+", content)
print('Nombre de mots présents dans le fichier : {}.'.format(len(res)))

