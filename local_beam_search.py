from heapq import heappush
from heapq import heappushpop
def local_beam_search(problem, k=5, limit=1000):
    front, seen = [], set()
    for i in range(k):
        current = problem.initial()
        front.append( (problem.value(current), current) )
    cnt = 0
    while front and cnt < limit:
        nextfront = []
        for val, node in front:
            neighbours = problem.children(node)
            for neighbour in neighbours:
                if neighbour not in seen:
                    seen.add(neighbour)
                    value = problem.value(neighbour)
                    if value is 0:
                        print("local beam: %d" % cnt) # Print number of iter
                        return neighbour
                    if len(nextfront) < k:
                        heappush(nextfront, (value, neighbour))
                    else:
                        val, node = heappushpop(nextfront, (value, neighbour))
                        seen.remove(node)
        front = nextfront
        cnt += 1
    return current

import random
class BiasedLotteryPool:
    def __init__(self):
        self.presum = [0]
        self.elems = []
        self.seen = set()

    def add(self, elem, value):
        if elem in self.seen:
            return None
        self.elems.append(elem)
        self.presum.append(self.presum[-1] + value)
        self.seen.add(elem)

    def floor(self, array, target):
        left, right = 0, len(array) - 1
        while left <= right:
            center = (left + right) // 2
            if array[center] < target:
                left = center + 1
            else:
                right = center - 1
        return left - 1

    def pick(self, size):
        if len(self.elems) < size:
            return self.elems
        result, chosen = list(), set()
        while len(result) < size:
            rand = random.randrange(self.presum[-1])
            i = self.floor(self.presum, rand)
            if self.elems[i] not in chosen:
                result.append(self.elems[i])
                chosen.add(self.elems[i])
        return result

def stochastic_beam_search(problem, k=15, limit=1000):
    front = [problem.initial() for i in range(k)]
    cnt = 0
    total = problem.N * (problem.N - 1) // 2 + 1
    while front and cnt < limit:
        pool = BiasedLotteryPool()
        for node in front:
            neighbours = problem.children(node)
            for neighbour in neighbours:
                value = problem.value(neighbour)
                if value is 0:
                    print("stoch # of iter: %d" % cnt) # Print num of iter
                    return neighbour
                pool.add(neighbour, 1000000000 // (value - 1) ** 2)
        front = pool.pick(k)
        cnt += 1
    return current
