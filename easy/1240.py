#!/usr/bin/env python

num = int(raw_input())
for i in range(num):
    li = list(raw_input())
    print "String #%d" %(i+1)
    print "".join(map(lambda x: 'A' if x == 'Z' else chr(ord(x)+1), li))
    print

