#!/usr/bin/env python

def caculate(li):
    result = li[0][0] * li[0][1]
    for i in range(1, len(li)):
        result += (li[i][1] - li[i-1][1]) * li[i][0]
    return result

num = int(raw_input())
while num != -1:
    li = []
    for i in range(num):
        li.append([int(x) for x in raw_input().split()])
    print "%d miles" %caculate(li)
    num = int(raw_input())

