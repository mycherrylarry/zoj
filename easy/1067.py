#!/usr/bin/env python
import sys, math
from operator import eq
li = []
for i in range(16):
    li.append([int(x) for x in raw_input().split()])

def distance(la, lb):
    return sum(map(lambda x, y: pow(x-y, 2), la, lb))

for line in sys.stdin:
    test = [int(x) for x in line.split()]
    if (all(map(eq, test, [-1,-1,-1]))):
        break
    min = li[-1]
    for item in li[:-1]:
        if distance(test, min) > distance(test, item):
            min = item 
    print "("+",".join([str(x) for x in test])+") maps to ("+",".join([str(x) for x in min])+")"

