#!/usr/bin/env python
import sys, math
n = int(raw_input())
for i in xrange(n):
    li = raw_input().split()
    x, y = float(li[0]), float(li[1])
    print "Property %d: This property will begin eroding in year %d." %(i+1, int(math.ceil((pow(x,2) + pow(y,2)) * math.pi / 100)))
print "END OF OUTPUT."
