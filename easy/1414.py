#!/usr/bin/env python
def numberStep(li):
    x, y = li
    if (x-y) == 2 or (x-y) == 0:
        if x%1 == 1:
            print x+y-1
        else:
            print x+y
    else:
        print "No Number"

num = int(raw_input())
for i in range(num):
    numberStep([int(x) for x in raw_input().split()])


