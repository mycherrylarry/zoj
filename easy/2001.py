#!/usr/bin/env python

def reverseInt(a):
    return int("".join(list(str(a))[::-1]))

num = int(raw_input())
for i in range(num):
    li = [int(x) for x in raw_input().split()]
    print "%d" %reverseInt(reverseInt(li[0]) + reverseInt(li[1]))
