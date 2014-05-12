#!/usr/bin/env python

def process(n, li):
    mp = [0]*(n-1)
    for i in range(1, n):
        if abs(li[i]-li[i-1]) < n:
            mp[abs(li[i]-li[i-1])-1] = 1
    return all(mp)


line = raw_input()
while line:
    li = [int(x) for x in line.split()]
    if process(li[0], li[1:]):
        print "Jolly"
    else:
        print "Not jolly"
    line = raw_input()
