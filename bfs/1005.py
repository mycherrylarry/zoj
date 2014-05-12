#!/usr/bin/env python
"""
Broad first search for Pouring Water problem

Another solution, could be implemented in DFS
http://www.cnblogs.com/wisdomqq/archive/2009/09/22/1571520.html
"""

class Jugs:
    #A is the capacity of cup A, T is the target volumn we need
    def __init__(self, A, B, T):
        self.A, self.B, self.T = A, B, T
        #store the volumn of (a, b)'s change route and the action type
        #self.route=[(a1,b1,2), (a2,b2,3) ...]
        self.route = []
        self.status = (0, 0)
        self.actionNames = {0:"fill A", 1:"file B", 2:"empty A", 3:"empty B", 4:"pour A B", 5:"pour B A"}
        self.actions = [self.fillA, self.fillB, self.emptyA, self.emptyB, self.pourAB, self.pourBA]

    def fillA(self):
        pass
    def fillB(self):
        pass
    def emptyA(self):
        pass
    def emptyB(self):
        pass
    def pourAB(self):
        pass
    def pourBA(self):
        pass

    def solve(self):
        queue = [self.fileA]
        while (len(queue)!=0):


jugs = Jugs(1,1,1)

