#!/usr/bin/env python

def convertToI(P):
    result = [0]*len(P)
    for i in range(len(P)):
        result[P[i]-1] = str(len(filter(lambda x: x> P[i], P[:i])))
    return result

def convertToP(I):
    result = []
    for i in range(len(I))[::-1]:
        result.insert(I[i], str(i+1))
    return result


n = int(raw_input())
while n:
    li = raw_input().split()
    if li[0] == 'P':
        print " ".join(convertToI([int(x) for x in li[1:]]))
    else:
        print " ".join(convertToP([int(x) for x in li[1:]]))
    n = int(raw_input())

