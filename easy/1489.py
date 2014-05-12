#!/usr/bin/env python

n = int(raw_input())
while n!=0:
    if n%2 == 0:
        print "2^? mod %d = 1" %n
    else:
        i = 2
        counter = 1
        while (i)%n != 1:
            counter += 1
            i = i << 1
            i %= n
        print "2^%d mod %d = 1" %(counter,n)
    n = int(raw_input())

        
