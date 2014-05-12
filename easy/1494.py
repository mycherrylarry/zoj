#!/usr/bin/env python
from operator import eq

def climbingWorm(li):
    n,u,d = li
    x = (n-2*u) / (u-d)
    while not ((u-d)*x >= (n-u) and (u-d)*x < (n-d)):
        x += 1
    print x*2+1

line = [int(x) for x in raw_input().split()]
while not all(map(eq, line, [0,0,0])):
    climbingWorm(line)
    line = [int(x) for x in raw_input().split()]
