#!/usr/bin/env python
import math
def dfs(a,b):
    if a<b:
        a,b = b,a
    if b == 0:
        return a
    return dfs(b, a%b)

num = int(raw_input())
while num!=0:
    li = []
    total = 0
    for i in xrange(num):
        li.append(int(raw_input()))
    for i in xrange(num-1):
        for j in xrange(i,num):
            if dfs(li[i], li[j])== 1:
                total += 1
    if total == 0:
        print "No estimate for this data set."
    else:
        print "%.6f" % math.sqrt(num*(num-1)*3/total)
    num = int(raw_input())
