#!/usr/bin/env python

def exchange(li, i, j):
    if i >= len(li):
        return
    while i < j:
        li[i], li[j] = li[j], li[i]
        i += 1
        j -= 1

def solve(li, n):
    for i in range(0, len(li), 2*n):
        exchange(li, i+n, i+2*n-1)

    result = []

    for i in range(n):
        result.extend(li[i::n])
    return "".join(result)


n=int(raw_input())
while n != 0:
    s=raw_input()
    print solve(list(s), n)
    n=int(raw_input())
