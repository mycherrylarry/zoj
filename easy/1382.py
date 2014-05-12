#!/usr/bin/env python
def simpleTask(n):
    p = 0
    while(n%2 == 0):
        p += 1
        n /= 2
    print "%d %d" %(n, p)

num = int(raw_input())
for i in xrange(num):
    simpleTask(int(raw_input()))
