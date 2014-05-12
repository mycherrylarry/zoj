#!/usr/bin/env python

def caculate(li):
    result = 6*li[0] + 5
    for i in range(1, len(li)):
        tmp = li[i] - li[i-1]
        if tmp > 0:
            result += tmp*6
        else:
            result += abs(tmp)*4
        result += 5
    return result

line = raw_input()
while line != '0':
    li = [int(x) for x in line.split()]
    print caculate(li[1:])
    line = raw_input()
