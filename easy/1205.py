#!/usr/bin/env python

def convertToStr(li):
    return map(lambda x: chr(ord('a')+x-10) if x>9 else str(x), li)

def convertToInt(li):
    return map(lambda x: ord(x)-ord('a')+10 if ord(x)>=ord('a') else int(x), li)

def adds(la, lb):
    li = []
    i, tmp = 0, 0
    while(i < len(la) and i < len(lb)):
        li.append((la[i] + lb[i] + tmp)%20)
        tmp = (la[i] + lb[i] + tmp) / 20
        i = i+1
    if i==len(la):
        while(i<len(lb)):
            li.append((lb[i]+tmp)%20)
            tmp = (lb[i]+tmp) / 20
            i=i+1
    else:
        while(i<len(la)):
            li.append((la[i]+tmp)%20)
            tmp = (la[i]+tmp) / 20
            i=i+1
    if tmp != 0:
        li.append(tmp)
    print "".join(convertToStr(li)[::-1])

import sys
tag = 0
la , lb = [], []
for line in sys.stdin:
    if tag == 0:
        la = list(line.strip())[::-1]
        tag = 1
        continue
    tag = 0
    lb = list(line.strip())[::-1]
    adds(convertToInt(la), convertToInt(lb))

