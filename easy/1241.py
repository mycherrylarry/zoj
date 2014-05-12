#!/usr/bin/env python
import sys, math
from operator import eq

i = 0
for line in sys.stdin:
    i = i+1
    li = [int(x) for x in line.split()]
    if all(map(eq, li, [0,0,0])):
        break
    print "Triangle #%d" %i
    a, b, c = li
    if a == -1:
        if c <= b:
            print "Impossible."
        else:
            print "a = %.3f" %(math.sqrt(pow(c, 2)-pow(b, 2)))
    elif b == -1:
        if c <= a:
            print "Impossible."
        else:
            print "b = %.3f" %(math.sqrt(pow(c, 2)-pow(a, 2)))
    else:
        print "c = %.3f" %(math.sqrt(pow(a, 2)+pow(b, 2)))
    print
