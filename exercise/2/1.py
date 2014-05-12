#!/usr/bin/env python
import sys
for line in sys.stdin:
    n = int(line.strip())
    i = 0
    while(n > 0):
        n = n/10
        i = i + 1
    print i



