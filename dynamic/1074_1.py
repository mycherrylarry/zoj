#!/usr/bin/env python

# By solving liner max subproblems

def maxSubLiner(li):
    n = len(li)
    route = [0]*(n+1)
    route[0] = -10000000
    for i in range(1, n+1):
        route[i] = max(li[i-1], route[i-1]+li[i-1])
    return max(route)

def maxSubMulti(mli):
    totalMax = 0
    l = len(mli)
    for i in range(l):
        for j in range(i, l):
            subLiner = adds(mli, i, j)
            subMax = maxSubLiner(subLiner)
            totalMax = max(subMax, totalMax)
    return totalMax

def adds(mli, i, j):
    return [sum(x) for x in zip(mli[i:j+1])]
    
num = int(raw_input())
li = []
while(len(li) < (num*num)):
    line = raw_input().split()
    li.extend([int(x) for x in line])

li = li[:(num*num)]
mli = []
for i in range(num):
    mli.append(li[i*num:(i*num + num)])

print maxSubMulti(mli)

