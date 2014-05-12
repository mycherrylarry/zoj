#!/usr/bin/env python

num = int(raw_input())
for i in range(num):
    n = int(raw_input())
    times = n/2*(n/2-1)/2+(n-n/2)*(n-n/2-1)/2
    print times
