from random import choice
class SearchProblem:
    def __init__(self, initial=None):
        """Initialize a search problem with a initial state"""
        pass

    def initial(self):
        """Return default initial state of the search problem"""
        pass

    def goal_test(self, state):
        """Return True if the state is a goal"""
        pass

    def value(self, state):
        """For optimization problems, each state has a value to be maximized"""
        pass

    def children(self, state):
        """Return children of the given state"""
        pass

    def random_child(self, state):
        """Return a random child of the state, used in simulated annealing"""
        return choice(self.children(state))

from collections import defaultdict
from collections import Counter
from random import randrange
class NQueensSearch(SearchProblem):
    '''
    State: ([QueenCoords], (shu, pie, na), val)
    '''
    def __init__(self, N):
        self.N = N

    def initial(self):
        return tuple(randrange(self.N) for i in range(self.N))

    def goal_test(self, state):
        shu, pie, na = (set() for i in range(3))
        for row, col in enumerate(state):
            if col in shu or row - col in pie or row + col in na:
                return False
            shu.add(col)
            pie.add(row - col)
            na.add(row + col)
        return True

    def value(self, state):
        """ -Number of pairs of queens attacking each other """
        shu, pie, na = [Counter() for i in range(3)]
        for row, col in enumerate(state):
            shu[col] += 1
            pie[row - col] += 1
            na[row + col] += 1
        clashes = 0
        for cnt in [shu, pie, na]:
            for key in cnt:
                clashes += cnt[key] * (cnt[key] - 1) // 2
        return -clashes

    def children(self, state):
        children = []
        for row in range(self.N):
            for col in range(self.N):
                if col != state[row]:
                    child = list(state)
                    child[row] = col
                    children.append(tuple(child))
        return children

    def random_child(self, state):
        row = randrange(self.N)
        col = randrange(self.N - 1)
        if col >= state[row]:
            col += 1
        child = list(state)
        child[row] = col
        return tuple(child)
