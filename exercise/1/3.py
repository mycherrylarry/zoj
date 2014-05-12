#!/usr/bin/env python
import sys

for line in sys.stdin:
    n = int(line.strip())
    print n*(1+n)/2
