# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:33:57 2020

@author: straw
"""

class Person:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
    
    def print_title(self):
        print('Le titre du livre est {}'.format(self.titre))

class Auteur(Person):
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.oeuvre = []
    
    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvre.append(livre.titre)
    
    def listerOeuvre(self):
        print(self.oeuvre)
        
bob = Auteur('Bob', 'Dylan')

bob.ecrireUnLivre('SDA 1')

bob.ecrireUnLivre('SDA 2')

bob.ecrireUnLivre('SDA 3')

bob.listerOeuvre()


                
        