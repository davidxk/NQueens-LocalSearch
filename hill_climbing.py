import random

def hill_climbing(problem):
    # Keep choosing the neighbour with highest value until no neighbor is better
    current = problem.initial()
    while True:
        neighbours = problem.children(current)
        if not neighbours:
            break
        neighbour = max(neighbours,
                key=lambda state: (problem.value(state), random.random()))
        if problem.value(neighbour) <= problem.value(current):
            break
        current = neighbour
    return current

def random_restart(problem, limit = 10):
    state = problem.initial()
    cnt = 0
    while problem.goal_test(state) == False and cnt < limit:
        state = hill_climbing(problem)
        cnt += 1
    return state
