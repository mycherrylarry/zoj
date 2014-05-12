#!/usr/bin/env python

def caculate(li):
    avg = float(sum(li))/len(li)
    return float(len(filter(lambda x : x>avg, li)))/len(li)

num = int(raw_input())
for i in range(num):
    li = [int(x) for x in raw_input().split()]
    print "%.3f%%" %(caculate(li[1:])*100)
