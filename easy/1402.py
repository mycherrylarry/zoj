#!/usr/bin/env python

def meatball(li):
    total = sum(li)
    if total%2 == 1:
        print "No equal partitioning."
        return
    tmp = 0
    for i in range(len(li)):
        if tmp < total/2:
            tmp += li[i]
        else:
            break
    if tmp > total/2:
        print "No equal partitioning."
        return
    print "Sam stops at position %d and Ella stops at position %d." %(i, i+1)

tag = raw_input()
while tag != '0':
    meatball([int(x) for x in tag.split()[1:]])
    tag = raw_input()
