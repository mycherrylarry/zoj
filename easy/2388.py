#!/usr/bin/env python

num = int(raw_input())
for i in range(num):
    li = [int(x) for x in raw_input().split()]
    x, y = li
    s = x+y
    m = x-y
    if m<0:
        print "impossible"
    else:
        print s/2, m/2
