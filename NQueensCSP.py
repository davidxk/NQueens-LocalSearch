class CSP(object):
    def __init__(self, variables = [], adjList = {}, domains = {}):
        self.variables = variables
        self.adjList = adjList
        self.domains = domains

    def nconflicts(self, X1, x, assignment):
        """
        Return the number of conflicts X1 = x has with other variables
        Subclasses may implement this more efficiently
        """
        def conflict(X2):
            return self.conflicts(X1, x, X2, assignment[X2])
        return sum(conflict(X2) for X2 in self.adjList[X1] if X2 in assignment)

    def conflicted_vars(self, current):
        """ Return a list of variables in conflict in current assignment """
        return [var for var in self.variables
                if self.nconflicts(var, current[var], current) > 0]

class NQueensCSP(CSP):
    def conflicts(self, row1, col1, row2, col2):
        return col1 == col2 or row1 + col1 == row2 + col2 or \
                row1 - col1 == row2 - col2
