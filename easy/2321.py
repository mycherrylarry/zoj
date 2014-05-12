#!/usr/bin/env python

mp = []
mp.append([4.5, 150, 200, 'Wide Receiver'])
mp.append([6.0, 300, 500, 'Lineman'])
mp.append([5.0, 200, 300, 'Quarterback'])

from operator import eq

li = [float(x) for x in raw_input().split()]
while not all(map(eq, li, [0, 0, 0])):
    x = filter(lambda x: li[0]<=x[0] and li[1]>=x[1] and li[2]>=x[2], mp)
    if len(x) == 0:
        print 'No positions'
    else:
        for item in x:
            print item[3],
    print
    li = [float(x) for x in raw_input().split()]

