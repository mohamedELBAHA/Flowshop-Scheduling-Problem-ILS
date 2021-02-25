#!/usr/bin/env python



import job
import ordonnancement


# On utilise une file de priorité pour les sommets : on peut
# ainsi accéder à tout moment au sommet de plus petite évaluation
import heapq

# valeurt maximale d'un entier
MAXINT = 10000

class Flowshop():
    def __init__(self, nombre_jobs=0, nombre_machines=0, liste_jobs=None):
        # nombre de jobs pour le problème
        self.nombre_jobs = nombre_jobs
        # nombre de machines pour le problème
        self.nombre_machines = nombre_machines
        # ensemble des jobs pour le problème (l'ordre n'est pas important)
        self.liste_jobs = liste_jobs
        
    def definir_par_fichier(self, nom):
        """ crée un problème de flowshop à partir d'un fichier """
        # ouverture du fichier en mode lecture
        fdonnees = open(nom,"r")
        # lecture de la première ligne
        ligne = fdonnees.readline() 
        l = ligne.split() # on récupère les valeurs dans une liste
        self.nombre_jobs = int(l[0])
        self.nombre_machines = int(l[1])
       
        self.liste_jobs = []
        for i in range(self.nombre_jobs):
            ligne = fdonnees.readline() 
            l = ligne.split()
            # on transforme la suite de chaînes de caractères représentant
            # les durées des opérations en une liste d'entiers
            l = [int(i) for i in l]
            j = job.Job(i, l)
            self.liste_jobs.append(j)
        # fermeture du fichier
        fdonnees.close()
        