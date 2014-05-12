#!/usr/bin/env python

def group(li):
    result = {}
    for item in li:
        if not result.has_key(item):
            result[item] = 1
        else:
            result[item] = result[item] + 1
    return result

def factorial(n):
    return n == 0 and 1 or reduce(lambda x, y: x*y, range(1, n+1))

def c(a, b):
    return factorial(b) / (factorial(b-a) * factorial(a))

def main(li):
    total = sum(li)
    g = group(li)
    result = 1
    for (k, v) in g.items():
        result = result * c(k, total) / v
        total = total - (k*v)
    return result

n = int(raw_input())
while n:
    li = [int(x) for x in raw_input().split()]
    print main(li)
    n = int(raw_input())
