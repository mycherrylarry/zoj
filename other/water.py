#!/usr/bin/env python
""" Given a array with random numbers, which presents bars of a city.
One day, a big ran fall into the city, caculate the total amount of water
that can be hold in the city"""
"""
      ||
||    ||
|| || ||
||_||_||_||
"""
def caculate(li):
    sm, mx = 0, max(li)
    for item in li: sm += (mx - item)
    i, j = 0, len(li) - 1
    mi = li[i]
    while li[i] < mx:
        if li[i]> mi:
            mi = li[i]
        sm -= (mx - mi)
        i += 1
    mi = li[j]
    while li[j] < mx:
        if li[j]> mi:
            mi = li[j]
        sm -= (mx - mi)
        j -= 1
    return sm

print caculate([3,2,3,4,100,0,100,1,30])

