#!/usr/bin/env python
from operator import eq
line = [int(x) for x in raw_input().split()]
while not all(map(eq, line, [0,0])):
    n, m = line
    li = [int(x) for x in raw_input().split()]
    tmp = [0]*(n+1)
    for item in li:
        tmp[item] += 1
    result = 0
    for item in tmp:
        if item > 1:
            result += 1
    print result
    line = [int(x) for x in raw_input().split()]

