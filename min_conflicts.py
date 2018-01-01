import random
from sys import stdout

def min_conflicts_value(csp, X, assignment):
    # Return the value that will give var the least number of conflicts.
    random.shuffle(csp.domains[X])
    return min(csp.domains[X], key=lambda x: csp.nconflicts(X, x, assignment))

def min_conflicts(csp, max_steps=1000):
    # Solve a CSP by stochastic hillclimbing on the number of conflicts.
    # Generate a complete assignment for all variables (probably with conflicts)
    assignment={}
    for X in csp.variables:
        val = min_conflicts_value(csp, X, assignment)
        assignment[X] = val
    # Now repeatedly choose a random conflicted variable and change it
    for i in range(max_steps):
        conflicted = csp.conflicted_vars(assignment)
        if not conflicted:
            stdout.write("\r")
            return assignment
        X = random.choice(conflicted)
        val = min_conflicts_value(csp, X, assignment)
        assignment[X] = val
        stdout.write( "\rProgress: " + "%d/%d" % (i + 1, max_steps) )
        stdout.flush()
    return None
