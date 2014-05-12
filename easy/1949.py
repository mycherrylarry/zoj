#!/usr/bin/env python

def caculate(l, li):
    row = map(lambda x: x%2==0, [sum(x) for x in li])
    sumOfCol = []
    for i in range(l):
        s = 0
        for j in range(l):
            s += li[j][i]
        sumOfCol.append(s)
    col = map(lambda x: x%2==0, sumOfCol)
    if all(row) and all(col):
        print "OK"
    elif row.count(False)>1 or col.count(False)>1:
        print "Corrupt"
    else:
        print "Change bit (%d,%d)" %(row.index(False)+1, col.index(False)+1)


num = int(raw_input())
while num != 0:
    li = []
    for i in range(num):
        li.append([int(x) for x in raw_input().split()])
    caculate(num, li)
    num = int(raw_input())



