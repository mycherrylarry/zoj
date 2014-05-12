#!/usr/bin/env python
class Cheese:
    def __init__(self, n, k, V):
        self.n = n
        self.k = k
        self.V = V
        self.route = [[0]*n for i in range(n)]
        self.mx = 0
        self.msn = self.mapSetN(n)

    def mapSetK(self,k, x, y):
        s = set([(x,y+k),(x,y-k),(x+k,y),(x-k,y)])
        for i in range(1, k):
            s.add((x+i, y+k-i))
            s.add((x+i, y+i-k))
            s.add((x-i, y+k-i))
            s.add((x-i, y+i-k))
        return s

    def mapSetN(self, n):
        s = set()
        for i in range(n):
            for j in range(n):
                s.add((i,j))
        return s
    
    def neibor(self, x,y):
        msn = self.msn
        k = self.k
        V = self.V
        reachable = self.mapSetK(k, x, y) & msn
        result = []
        for item in reachable:
            a,b = item
            if self.route[a][b] == 0:
                if V[x][y] < V[a][b]:
                    result.append(item)
        return result
    
    def solve(self, x, y, counter):
        V = self.V
        counter += V[x][y]
        neib = self.neibor(x,y)
        if len(neib) == 0:
            if counter > self.mx:
                self.mx = counter
                return
        for item in neib:
            a, b = item
            self.route[a][b] = 1
            self.solve(a, b, counter)
            self.route[a][b] = 0
    
from operator import eq
line = [int(x) for x in raw_input().split()]
while not all(map(eq, line, [-1,-1])):
    V = []
    for i in range(line[0]):
        li = [int(x) for x in raw_input().split()]
        V.append(li)
    cheese = Cheese(line[0], line[1], V)
    cheese.solve(0,0,0)
    print cheese.mx
    line = [int(x) for x in raw_input().split()]

