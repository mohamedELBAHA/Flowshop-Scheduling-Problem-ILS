#!/usr/bin/env python
"""
Please Open [Ordonnacement.py, job.py, flowshop,py ] in your editor so the methods could be imported 

"""

__author__ = 'Mohamed EL BAHA'

import random
import copy
from ordonnancement import Ordonnancement
from job import Job
from flowshop import Flowshop

max_iteration=30
max_memory=10
R = 4



####################################################################
#                     GENERATE INITIAL SOLUTION                    #
####################################################################

def GenerateInitialSolution(liste_jobs, nombre_machines):
    lenght = len(liste_jobs)
    sequence = []
    while len(sequence)!=lenght:
        L = []
        for job in liste_jobs:
            sequence.append(job)
            ordo = Ordonnancement(nombre_machines)
            ordo.ordonnancer_liste_job(sequence)
            if len(L)==0:
                L.append([job, ordo.duree])
            for j in range(0,len(L)):
                if ordo.duree < L[j][1]:
                    L.insert(j,[job, ordo.duree])
            if len(L)>R:
                L.pop()
            sequence.pop()
        rang=random.randint(0,min(R-1, len(L)-1))
        job=L[rang][0]
        sequence.append(job)
        liste_jobs.remove(job)
    ordo = Ordonnancement(nombre_machines)
    ordo.ordonnancer_liste_job(sequence)
    return ordo

####################################################################
#                    LOCAL SEARCH ( TABOU ALGORITHM )              # 
####################################################################
def best_neighbor(ordo, last_solutions):                
    nombre_jobs = len(ordo.sequence)
    best_ordo = ordo
    for k in range(nombre_jobs-1):
        for i in range(k+1,nombre_jobs):
            sequence = copy.copy(ordo.sequence)
            sequence[k],sequence[i] = sequence [i],sequence[k]
            ordo2 = Ordonnancement(ordo.nombre_machines)
            ordo2.ordonnancer_liste_job(sequence)
            if best_ordo == ordo and (ordo2.sequence not in last_solutions):
                best_ordo = ordo2
            if ordo2.duree < best_ordo.duree and (ordo2.sequence not in last_solutions):
                best_ordo = ordo2
    return best_ordo

def LocalSearch(liste_jobs, nombre_machines):
    """     TABOU Algorithm    """
    S = Ordonnancement(nombre_machines) 
    S.ordonnancer_liste_job(liste_jobs) # Generating a starting solution     
    S_best = S # Updating best solution found so far  
    last_solutions = [S.sequence] # Initializing a list containting Last solutions
    i = 0
    while i < max_iteration : #  stop criterion :  maximum number of iterations is achieved 
        S = best_neighbor(S, last_solutions) # Test and update better solution
        if S.duree < S_best.duree:
            S_best = S
        
        last_solutions.append(S.sequence)
        if len(last_solutions) > max_memory:
            last_solutions.pop(0)
        i+=1
    return S_best
####################################################################
#                         PERTURBATION                             #
####################################################################
def perturbation(ordo):  # Swap + Reversion perturbation ( should be strong enought to o kick-out the solution from the local optima) 
    sequence = copy.copy(ordo.sequence)
    center = len(sequence)//2 # Look for the center of the List
    demi_seq1 = sequence[:center] # Divid the sequence into two equal parts ( left and right)
    demi_seq2 = sequence[center:]
    demi_seq1.reverse() # reverse the right part
    sequence_bis=demi_seq2+demi_seq1 # re-organised the whole sequence
    ordo_changed = Ordonnancement(ordo.nombre_machines)
    ordo_changed.ordonnancer_liste_job(sequence_bis)
    return ordo_changed
####################################################################
#                       ACCEPTANCE CRIETERION                      #
####################################################################
def AcceptanceCriterion(ordo1, ordo2):
    if ordo2.duree < ordo1.duree: 
        return ordo2
    else:
        return ordo1
####################################################################
#                       ITERATED LOCAL SEARCH                      #
####################################################################
def IteratedLocalSearch(liste_jobs, nombre_machines):
    So = GenerateInitialSolution(liste_jobs,nombre_machines) # So is the initial solution  
    S_op = LocalSearch(So.sequence, nombre_machines) #  Initial solution So is intensified to reach a local optimum S_op
    i=0
    while i < max_iteration : # stop criterion :  maximum number of iterations is achieved 
        S_prime = perturbation(S_op) # perturbs the solution to escape local optima, S_prime is the changed optimal solution.
        S_prime_op = LocalSearch(S_prime.sequence, nombre_machines) # uses LocalSearch method to find the new local optima S_prime_op.
        S_op = AcceptanceCriterion(S_op, S_prime_op) # Test and update, accepts non improving solutions along the process.
        i+=1
    return S_op

"""
----------------------------------------------------------------------------------------------------------------

Use one of the following methods to execute the code : 
    - First method to execute test .txt files one by one and changing manulay the name ( tai01 , tai02 ... etc).
    - Second method use a for loop to execute all the existing test .txt files, no need to change the name. 

----------------------------------------------------------------------------------------------------------------
"""

                
#----------------- | Method 1 |-------------------------------
                              

prob = Flowshop()
prob.definir_par_fichier('tai01.txt')
result=IteratedLocalSearch(prob.liste_jobs, prob.nombre_machines)
print(' - Ordonnancement optimal  =  |', end=" ")
for j in result.sequence:
    print(j.numero, end=" ")
print("| - durée = ", result.duree)



               
#--------------------| Method 2 |-------------------------------

"""
prob = Flowshop()
prob.definir_par_fichier('tai01.txt')
string = "tai01.txt"
for i in [0,1,2,3,4,5]:
    for j in [1,2]:    
        string = list(string)
        string[3] = format(i)
        string[4] = str(j)
        string = "".join(string)
        prob.definir_par_fichier(string)
        print(' - Jeu de données : taille',string[3],string[4])
        result = IteratedLocalSearch(prob.liste_jobs, prob.nombre_machines)
        print(' - Ordonnancement optimal : |', end="")
        for j in result.sequence:
            print(j.numero, end = " ")
        print("| - durée = ", result.duree)        
        print()
"""