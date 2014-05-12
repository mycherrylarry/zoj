#!/usr/bin/env python

num = int(raw_input())
for i in range(num):
    li = [int(x) for x in raw_input().split()]
    if li[0] < li[1]:
        print "NO BRAINS"
    else:
        print "MMM BRAINS"

