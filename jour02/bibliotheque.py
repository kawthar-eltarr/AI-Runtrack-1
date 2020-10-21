# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:54:44 2020

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

class bibliotheque(Auteur):
    def __init__(self):
        self.nom
        self.catalogue = {'titre_livre' : [], 'quantite' : []}
        
    def acheterLivre(self, auteur, titre, quantite):
        if titre in auteur.oeuvre:
            self.catalogue['titre_livre'].append(titre)
            self.catalogue['quantite'].append(quantite)
    
    def inventaire(self):
        print('Voici les livres en inventaire :')
        print(self.catalogue)
    
    def louer(self):
        return 0
    
    def rendreLivres(self):
        return 0
        