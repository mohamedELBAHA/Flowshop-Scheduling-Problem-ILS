#!/usr/bin/env python


from job import Job





class Ordonnancement:

    # constructeur pour un ordonnancement vide
    def __init__(self, nombre_machines):
        # liste des jobs dans l'ordre où ils doivent être ordonnancés
        self.sequence = []

        # nombre de machines utilisées
        self.nombre_machines = nombre_machines

        # durée de l'ordonnancement, c'est-à-dire date de fin de la dernière
        # opération exécutée
        self.duree = 0

        # pour chaque machine, date à partir de laquelle on peut exécuter une
        # nouvelle opération.
        # Les machines sont numérotées à partir de 0
        self.date_disponibilite = [0 for i in range(self.nombre_machines)]

    def sequence(self):
        return self.sequence

    def nombre_machines(self):
        return self.nombre_machines

    def duree(self):
        return self.duree

    def date_disponibilite(self, machine):
        return self.date_disponibilite[machine]

    def changer_date_disponibilite(self, date, machine):
        self.date_disponibilite[machine] = date

    def fixer_date_debut(self, job, operation, date):
        job.date_debut[operation] = date


    def afficher(self):
        print("Ordre des jobs :", end='')
        for job in self.sequence:
            print(" ",job.numero," ", end='')
        print()
        for job in self.sequence:
            print("Job", job.numero, ":", end='')
            for machine in range(self.nombre_machines):
                print(" op", machine,
                      "à t =", job.date_debut[machine],
                      "|", end='')
            print()
        print("Cmax =", self.duree)

    def ordonnancer_job(self, job):
        self.sequence.append(job)
        #On va l'ajouter d'abord le job dans la machine 1
        self.fixer_date_debut(job, 0, self.date_disponibilite[0]) #On change la date de début de l'opération
        self.changer_date_disponibilite(job.date_debut[0] + job.duree_operation[0], 0) #On change la date de disponibilite de la machine
        #Ensuite on ajoute le job dans les autres machines
        if self.nombre_machines > 0:
            for i in range(1, self.nombre_machines):
                if self.date_disponibilite[i] > job.date_debut[i-1] + job.duree_operation[i-1]:
                    self.fixer_date_debut(job, i, self.date_disponibilite[i])
                    self.changer_date_disponibilite(job.date_debut[i] + job.duree_operation[i], i)
                else:
                    self.fixer_date_debut(job, i, job.date_debut[i-1] + job.duree_operation[i-1])
                    self.changer_date_disponibilite(job.date_debut[i] + job.duree_operation[i], i)


        self.duree = job.date_debut[self.nombre_machines -1] + job.duree_operation[self.nombre_machines-1]
    
    #Ordonnance les jobs de la liste au plus tôt et dans l'ordre de la liste (On tiendra compte des jobs déjà présents dans la liste)
    def ordonnancer_liste_job(self, liste_jobs):
        for job in liste_jobs:
            self.ordonnancer_job(job)


# Pour tester
if __name__ == "__main__":
    a = Job(1,[1,1,1,10,1])
    b = Job(2,[1,10,1,1,1])
    a.afficher()
    b.afficher()
    l = [a,b]
    ordo = Ordonnancement(5)
    ordo.ordonnancer_job(a)
    ordo.ordonnancer_job(b)
    # ordo.ordonnancer_liste_job([a,b])
    ordo.sequence
    ordo.afficher()
    a.afficher()
    b.afficher()

