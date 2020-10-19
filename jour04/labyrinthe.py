# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:56:20 2020

@author: straw
"""
import re

file = open("maze.mz", "r")
maze = file.read()
file.close()

entrance = maze[0:3]
exit = maze[len(maze)-4:len(maze)-1]

re.search('', maze)