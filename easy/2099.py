#!/usr/bin/env python
from operator import eq

line = [int(x) for x in raw_input().split()]
while not all(map(eq, line, [0,0])):
    li = []
    while not all(map(eq, line, [0,0])):
        li.append(line)
        line = [int(x) for x in raw_input().split()]
    w = min([li[i][0] for i in range(len(li))])
    s = min([li[i][1] for i in range(len(li))])
    e = max([li[i][0] for i in range(len(li))])
    n = max([li[i][1] for i in range(len(li))])
    print w,s,e,n
    line = [int(x) for x in raw_input().split()]

