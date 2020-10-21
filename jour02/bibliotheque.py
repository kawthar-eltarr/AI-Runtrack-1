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

class Client(Person):
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.collection = []

    def inventaire_client(self):
        print('Voici les livres en inventaire du client :')
        print(self.collection)


class Bibliotheque():
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {'titre_livre' : [], 'quantite' : []}
        
    def acheterLivre(self, auteur, titre, quantite):
        if titre in auteur.oeuvre:
            if titre in self.catalogue['titre_livre']:
                self.catalogue['quantite'][self.catalogue['titre_livre'].index(titre)] = self.catalogue['quantite'][self.catalogue['titre_livre'].index(titre)] + quantite
            else:
                self.catalogue['titre_livre'].append(titre)
                self.catalogue['quantite'].append(quantite)
    
    def inventaire(self):
        print('Voici les livres en inventaire de la biliothèque :')
        print(self.catalogue)
    
    def louer(self, client, titre):
        if titre in self.catalogue['titre_livre']:
            client.collection.append(titre)
    
    def rendreLivres(self, client):
        for L in client.colletion:
            if L in self.catalogue['titre_livre']:
                self.catalogue['quantite'][self.catalogue['titre_livre'].index(L)] = self.catalogue['quantite'][self.catalogue['titre_livre'].index(L)] + client.colletion.count(L)
            else:
                self.catalogue['titre_livre'].append(L)
                self.catalogue['quantite'].append(client.colletion.count(L))
        client.collection = []


gaarder = Auteur('Jostein', 'Gaarder')
gaarder.ecrireUnLivre('Le Monde de Sophie')
gaarder.ecrireUnLivre('Dans un miroir, obscur')
gaarder.listerOeuvre()

coelho = Auteur('Paulo', 'Coelho')
coelho.ecrireUnLivre('L\'Alchimiste')
coelho.ecrireUnLivre('La Cinquième Montagne')
coelho.listerOeuvre()

khadra = Auteur('Yasmina', 'Khadra')
khadra.ecrireUnLivre('Ce que le jour doit à la nuit')
khadra.ecrireUnLivre('Les anges meurent de nos blessures')
khadra.ecrireUnLivre('Cousine K') 
khadra.listerOeuvre()

sapkowski = Auteur('Andrzej', 'Sapkowski')
sapkowski.ecrireUnLivre('Le Dernier Vœu')
sapkowski.ecrireUnLivre('L\'Épée de la providence')
sapkowski.ecrireUnLivre('Quelque chose s\'achève, quelque chose commence ')
sapkowski.listerOeuvre()

shakespeare = Auteur('William', 'Shakespeare')
shakespeare.ecrireUnLivre('Hamlet')
shakespeare.ecrireUnLivre('Romeo et Juliette')
shakespeare.ecrireUnLivre('Macbeth')

stoker = Auteur('Bram', 'Stoker')
stoker.ecrireUnLivre('Dracula')
stoker.listerOeuvre()

camus = Auteur('Albert', 'Camus')
camus.ecrireUnLivre('La peste')
camus.ecrireUnLivre('L\'Étranger')
camus.ecrireUnLivre('L\'Exil et le Royaume')
camus.listerOeuvre()
 
alcazar = Bibliotheque('Alcazar')

alcazar.acheterLivre(camus, 'La peste', 11)

alcazar.acheterLivre(khadra, 'Ce que le jour doit à la nuit', 10)

alcazar.acheterLivre(shakespeare, 'Romeo et Juliette', 4)

ezio = Client('Ezio', 'Auditore')

alcazar.louer(ezio, 'Dracula')
