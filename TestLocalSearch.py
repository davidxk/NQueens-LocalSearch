from time import time

class TestLocalSearch(object):
    def __make_board__(self, n, result):
        board = []
        for col in result:
            line = ['.'] * n
            line[col] = 'Q'
            board.append(str().join(line))
        return board

    def printBoard(self, board):
        charlist = map(list, board)
        for line in charlist:
            print " ".join(line)

    def testLocalSearch(self, problem, local_search):
        times = 10
        cnt = 0
        start = time()
        for i in range(times):
            result = local_search(problem)
            if problem.value(result) is 0:
                cnt += 1
        print " - Accuracy: %2d/%d\tRunning time: %f"%(cnt, times, time()-start)

from hill_climbing import hill_climbing
from hill_climbing import random_restart
from simulated_annealing import simulated_annealing
from local_beam_search import local_beam_search
from local_beam_search import stochastic_beam_search
from FastNQueen import fast_simulated_annealing
from NQueens import NQueensSearch
from FastNQueens import FastNQueens

if __name__ == "__main__":
    test = TestLocalSearch()
    print "Running local search for N Queens Problem"
    size = input(" - Please input the size of the board (4~15): ")
    print
    problem = NQueensSearch(size)
    algorithms = [fast_simulated_annealing, hill_climbing, random_restart,
            simulated_annealing, local_beam_search]
    names = ["fast_simulated_annealing", "hill_climbing", "random_restart",
            "simulated_annealing", "local_beam_search"]
    problems = [FastNQueens(size), problem, problem, problem, problem]
    for i in range(len(algorithms)):
        print names[i]
        board = test.testLocalSearch(problems[i], algorithms[i])
    # stochastic_beam_search runs rather slowly on large boards
    print "stochastic_beam_search"
    board = test.testLocalSearch(problem, stochastic_beam_search)
