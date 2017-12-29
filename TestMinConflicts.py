from NQueensCSP import NQueensCSP
from min_conflicts import min_conflicts

class MinConflictNQueensSolver:
    def __make_board__(self, n, result):
        board = []
        for i in range(n):
            line = ['.'] * n
            line[result[i]] = 'Q'
            board.append(str().join(line))
        return board

    def buildCspProblem(self, n):
        adjList = {}
        for i in range(n):
            adjList[i] = set([ j for j in range(n) if j != i ])
        domains = {}
        for i in range(n):
            domains[i] = range(n)
        return NQueensCSP(range(n), adjList, domains)

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        csp = self.buildCspProblem(n)
        result = min_conflicts(csp)
        return self.__make_board__(n, result)

if __name__ == "__main__":
    sol = MinConflictNQueensSolver()
    size = input("Please input the size of the board(4~300): ")
    board = sol.solveNQueens(size)
    charlist = map(list, board)
    for line in charlist:
        print " ".join(line)
