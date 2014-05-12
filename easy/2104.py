#!/usr/bin/env python

def process(li):
    d = dict((i, li.count(i)) for i in li)
    k, v = max(d.iteritems(), key=lambda x: x[1])
    return k

num = int(raw_input())
while num != 0:
    li = []
    for i in range(num):
        li.append(raw_input())
    print process(li)
    num = int(raw_input())
