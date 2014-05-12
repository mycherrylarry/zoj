#!/usr/bin/env python

num = int(raw_input())
for i in range(num):
    l, n = [int(x) for x in raw_input().split()]
    li = [int(x) for x in raw_input().split()]
    mi = l/2 - min(map(lambda x: abs(x-l/2), li))
    mx = l/2 + max(map(lambda x: abs(x-l/2), li))
    print mi , mx

