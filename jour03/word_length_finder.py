# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:48:03 2020

@author: straw
"""
import re

nb = int(input("Please select number desired : "))
file = open("data.txt", "r")
content = file.read()
file.close()
content = content.lower()
res = re.findall(r"\w+", content)

lengths = [len(r) for r in res]

filtered_lengths = [l for l in lengths if l == nb]

print('Nombre de mots présents dans le fichier dont la taille est {0} lettres : {1}.'.format(nb, len(filtered_lengths)))
