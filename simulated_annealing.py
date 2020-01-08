import random
import math
import sys

# -- Standard implementation of Simulated Annealing Algorithm -- #

# You've got to tune these parameters carefully before you can make it work
def exp_schedule(k=4, lam=0.001, limit=20000):
    # One possible schedule function for simulated annealing
    # Parameters must be tuned according to the size of the input
    # Tuned for 50 * 50 N Queens Problem
    # Another possible function could be 100*0.99^t
	# k decides the time span of random walk
	# lambda decides how steep does the probability converges to zero
	# limit decides the number of iterations
    return lambda t: (k * math.exp(-lam * t) if t < limit else 0)

# SA: A version of stochastic hill climbing where downhill moves are allowed
def simulated_annealing(problem, schedule=exp_schedule()):
    current = problem.initial()
    currVal = problem.value(current)
    for t in range(sys.maxsize):
        T = schedule(t)
        if T == 0 or problem.goal_test(current):
            return current
        neighbour = problem.random_child(current)
        if not neighbour:
            return current
        nextVal = problem.value(neighbour) 
        delta_e = nextVal - currVal
        if delta_e > 0 or random.uniform(0.0, 1.0) < math.exp(delta_e // T):
            current = neighbour
            currVal = nextVal
