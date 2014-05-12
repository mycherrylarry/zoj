#!/usr/bin/env python

def double(li):
    liD = [2*x for x in li]
    return len(set(li).intersection(set(liD)))

line = raw_input()
while line != '-1':
    li = [int(x) for x in line.split()]
    print double(li[:-1])
    line = raw_input()
