#!/usr/bin/env python
import sys
def fChangeToC(f):
    return 5*(float(f)-32)/9

for line in sys.stdin:
    f = line.strip()
    print "%.3f" % fChangeToC(f)
