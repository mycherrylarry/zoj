#!/usr/bin/env python

N = 2
li = []
li.append([5,9,1,4])
li.append([4,4,5,6])
li.append([6,8,5,4])
li.append([0,4,4,3])
route = []

def check(index):
    if index in route: return False
    n = len(route)
    x, y = n/N, n%N
    if x != 0:
        if li[route[n - N]][2] != li[index][0]: return False
    if y != 0:
        if li[route[n - 1]][1] != li[index][3]: return False
    return True


def solve(n):
    if n == N*N:
        print route
        return
    for index in range(len(li)):
        if check(index):
            route.append(index)
            solve(n+1)
            route.pop()

print li
print route
solve(0)
