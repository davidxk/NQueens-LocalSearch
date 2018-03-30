import random
from NQueens import NQueensSearch

# This is a fast implementation of N Queens problem with Simulated Annealing
#   where we calculate the value difference between a state and its neighbour
#   delta_e efficiently as we pick a random neighbour
class FastNQueens(NQueensSearch):
    def random_child(self, state):
        delta_clash = 0
        row = random.randrange(self.N)
        col = state[row]
        for r, c in enumerate(state):
            if r != row and ( c == col or r+c == row+col or r-c == row-col):
                delta_clash -= 1
        col = random.randrange(self.N - 1)
        if col >= state[row]:
            col += 1
        for r, c in enumerate(state):
            if r != row and ( c == col or r+c == row+col or r-c == row-col):
                delta_clash += 1
        child = list(state)
        child[row] = col
        return tuple(child), -delta_clash

import sys
import math

def fast_simulated_annealing(problem):
    current = problem.initial()
    value = problem.value(current)
    schedule = lambda t: max(120 * 0.95 ** t, 0.01)
    for t in xrange(sys.maxsize):
        T = schedule(t)
        if T == 0 or value == 0:
            return current
        neighbour, delta_e = problem.random_child(current)
        if not neighbour:
            return current
        if delta_e > 0 or random.uniform(0.0, 1.0) < math.exp(delta_e / T):
            current = neighbour
            value += delta_e
