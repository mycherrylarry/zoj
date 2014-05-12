#!/usr/bin/env python
import sys, math
for line in sys.stdin:
    li = line.strip().split()
    x1, y1, x2, y2 = [float(x) for x in li[:4]]
    print math.sqrt(abs(pow(x1,2)-pow(x2,2)) + abs(pow(y1,2)- pow(y2,2)))



