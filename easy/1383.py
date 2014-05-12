#!/usr/bin/env python
num = int(raw_input())
for x in range(num):
    n = int(raw_input())
    li = []
    while(n!=0):
        li.append(n%2)
        n = n>>1
    
    for i in range(len(li)):
        if li[i] == 1:
            print i,
