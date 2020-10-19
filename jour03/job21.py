# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:37:36 2020

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
