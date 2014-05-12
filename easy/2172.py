#!/usr/bin/env python

def resort(li):
    r = li[1::2]
    l = li[::2]
    r = r[::-1]
    return l+r


num = int(raw_input())
x = 1
while num != 0:
    li = []
    for i in range(num):
        li.append(raw_input())
    result = resort(li)
    print "SET %d" %x
    for item in result:
        print item
    num = int(raw_input())
    x += 1

