#!/usr/bin/env python
import math
from operator import eq

PI = math.pi
def caculate(D, V):
    return pow((pow(D, 3) - (6*V)/PI), 1.0/3.0)

line = [int(x) for x in raw_input().split()]
while not all(map(eq, line, [0,0])):
    print "%.3f" %caculate(line[0], line[1])
    line = [int(x) for x in raw_input().split()]
