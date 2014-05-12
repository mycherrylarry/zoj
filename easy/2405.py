#!/usr/bin/env python
def countBase(n, b):
    result = 0
    while (n/b) !=0:
        result += n%b
        n = n/b
    return result+n

for n in range(2991, 10000):
    a, b, c = countBase(n, 10), countBase(n, 12), countBase(n, 16)
    if a == b and a == c:
        print n
