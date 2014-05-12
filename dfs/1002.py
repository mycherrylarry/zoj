#!/usr/bin/env python

class FireNet:
    def __init__(self, li, n):
        self.li = li
        self.n = n
        self.max = 0
    
    def count(self, key):
        c = 0
        for item in self.li:
            c += item.count(key)
        return c

    def check(self, pos):
        x, y = pos
        li = self.li
        if li[x][y] == 'X': return False
        for i in range(x-1, -1, -1):
            if li[i][y] == 'X': break
            if li[i][y] == 'O': return False
        for i in range(y-1, -1, -1):
            if li[x][i]== 'X': break
            if li[x][i]== 'O': return False
        return True

    def solve(self, counter):
        n, li = self.n, self.li
        if counter == n*n:
            if self.count('O') > self.max:
                self.max = self.count('O')
            return
        x, y = counter/n, counter%n
        if self.check((x,y)):
            li[x][y] = 'O';
            self.solve(counter+1)
            li[x][y] = '.';
        self.solve(counter+1)

n = int(raw_input())
while(n != 0):
    li = []
    for i in xrange(n):
        raw = list(raw_input().strip())
        li.append(raw)
    fire_net = FireNet(li, n)
    fire_net.solve(0)
    print "%d" %(fire_net.max)
    n = int(raw_input())
