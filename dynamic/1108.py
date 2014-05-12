#!/usr/bin/env python

def binarySearch(li, item):
    left , right = 0, len(li)
    while left < right:
        mid = left + (right - left)/2
        if li[mid] >= item:
            right = mid
        else:
            left = mid + 1
    return left

def solve(li):
    b = []
    pre = []
    for i in range(len(li)):
        position = binarySearch([li[x] for x in b], li[i])
        if len(b) == position:
            if position == 0:
                pre.append(-1)
            else:
                pre.append(b[-1])
            b.append(i)
        else:
            pre.append(pre[b[position]])
            b[position] = i
    result = []
    t = b[-1]
    while t!=-1:
        result.append(t)
        t = pre[t]
    return result[::-1]

#print solve([4,3,5,1,7])
#print solve([1,2,3,4])
#print solve([4,3,2,1])
        

