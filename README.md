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
  S = LocalSearch(So)
  While stopping criterion not reached Do
    S = Perturbtion(S)
    S = LocalSearch()
    S = AceptanceCriterion(S,S)
  EndWhile
```
