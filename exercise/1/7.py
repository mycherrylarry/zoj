#!/usr/bin/env python
import sys

for line in sys.stdin:
    n = float(line.strip())
    total = n * 95
    if (total >= 300):
        total = total*0.85
    print "%.3f" % total

