#!/usr/bin/env python
def cacultate(li):
    x, y, z = li
    pi = 3.14159
    left = int((5*y)-(2*pi*x*z/360))
    if left >= 0:
        print "YES %d" % (left/5)
    else:
        print "NO %d" % (5*y)

line = raw_input()
while line!= 'ENDOFINPUT':
    cacultate([int(x) for x in raw_input().split()])
    raw_input()
    line = raw_input()
