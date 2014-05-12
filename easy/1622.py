#!/usr/bin/env python
def switch(li):
    n = len(li)
    v1 = len(li[::2]) - sum(li[::2]) + sum(li[1::2])
    v2 = n - v1
    return min(v1, v2)

print switch([1,0,0])
print switch([1,0,1,1])
print switch([0,1,0,1])


