#!/usr/bin/env python
import sys

for line in sys.stdin:
    li = line.split()
    total = reduce(lambda x,y: x+y, [float(x) for x in li])
    print "%.3f" %(total/3)
