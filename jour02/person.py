# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:06:30 2020

@author: straw
"""

class Person:
    def __init__(self, first_name='Lucas', last_name='Pommier'):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def set_first_name(self, first_name):
        self.first_name = first_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name
        
    def se_presenter(self):
        print('Enchanté, je m\'appelle {0} {1}.'.format(self.first_name, self.last_name))
      
# John se présente
john = Person('John', 'Smith')
john.se_presenter()

# Lucas (la valeur par défaut) se présente
lucas = Person()
lucas.se_presenter()

# Changer le nom par défaut à Martin 
person = Person()
person.set_first_name('Martin')
person.set_last_name('Bouvier')

# Martin se présente
person.se_presenter()

