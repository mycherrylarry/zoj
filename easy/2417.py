#!/usr/bin/env python

def solve(n):
    i = 1
    while (n & i) == 0:
        i = i << 1
    return i

n = int(raw_input())
while n :
    print solve(n)
    n = int(raw_input())
