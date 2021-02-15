## Flowshop_Scheduling_Problem_ILS
# Using iterated local search for solving the flowshop problem 
The permutation flowshop sequencing problem (PFSP) is a well-known scheduling problem that
can be described as follows: a set J of k-independent jobs has to be processed on a set M of machine
m-independent machines. Each job j ∈ J requires a given fixed processing time math  Pij ≥ 0  on each.
Iterated Local Search Method :
- Starts from a locally optimum
- Perturbs the solution to escape local optima
- Uses a Local Search method to find the new local optima
- Accepts non improving solutions along the process
The stopping criterion can be reaching a maximum number of iterations is achieved, or a maximum CPU time is reached, or a maximum number of non-improvements is reached. in our case we choose the number of iterations.
```python
IteratedLocalSearch:
  GenerateInitialSolution So 
  S* = LocalSearch(So) // Initial solution is intensified to reach a local optimum
  S𝑏𝑒𝑠𝑡 = S*
  While stopping criterion not reached Do
    S' = Perturbtion(S*) // Local optimum solution is diversified using PERTURBATION
    S*' = LocalSearch(S') // New local solution is found using Intensification MOVES
    S* = AceptanceCriterion(S*,S*') // New local optimum is conditionally ACCEPTED
  EndWhile
```
![Algorithm schema](https://github.com/mohamedELBAHA/Flowshop_Scheduling_Problem_ILS-/blob/main/Capture.JPG?raw=true)
