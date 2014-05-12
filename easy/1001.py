#!/usr/bin/env python
import sys
def add(li):
    print int(li[0]) + int(li[1])

for line in sys.stdin:
    a = line.split()
    add(a)
