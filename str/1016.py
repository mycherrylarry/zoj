#!/usr/bin/env python

def generator(li):
    x = 0
    s = []
    for item in li:
        for i in range(item - x):
            s.append('(')
        s.append(')')
        x = item
    return s

def counter(li):
    s = []
    r = []
    i = 1
    for item in reversed(li):
        if item == ')':
            s.append((i, 0))
            s = [(k, v+1) for (k, v) in s]
            i = i+1
            continue
        r.append(s.pop())
    return " ".join([str(v) for (k,v ) in sorted(r, key=lambda (x,y) :x, reverse=True)])

for i in range(int(raw_input())):
    raw_input()
    print counter(generator([int(x) for x in raw_input().split()]))
