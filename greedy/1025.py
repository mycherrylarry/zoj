#!/usr/bin/env python

def sticks(li):
    #li = [(4,9), (5,2), (2,1), (3,5), (1,4)]
    li =  sorted(li, key=lambda x: x[0])
    n = len(li)
    tags = [True]*n
    total = 0
    result = []
    while len(result)!=n:
        tmp = [i for i in range(n) if tags[i]]
        total += 1
        result.append(li[tmp[0]])
        tags[tmp[0]] = False
        for item in tmp[1:]:
            if li[item][0] >= result[-1][0] and li[item][1] >= result[-1][1]:
                result.append(li[item])
                tags[item] = False
    return total

num = int(raw_input())
for i in xrange(num):
    n = int(raw_input())
    line = [int(x) for x in raw_input().split()]
    li  = map(lambda x, y: (x,y), line[::2], line[1::2])
    print sticks(li)
