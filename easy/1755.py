#!/usr/bin/env python

def size(li):
    a, b, c = li[:3]
    return int(a)*int(b)*int(c)

def caculate(li):
    return min(li, key=size), max(li, key=size)

num = int(raw_input())
while num != -1:
    li = []
    for i in range(num):
        li.append(raw_input().split())
    mi, mx = caculate(li)
    print "%s took clay from %s." %(mx[-1], mi[-1])
    num = int(raw_input())

