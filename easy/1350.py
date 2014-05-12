#!/usr/bin/env python
import math

def isPrime(n):
    for i in xrange(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def countDivisor(n):
    if n == 1:
        return 1
    li = filter(isPrime, range(2,100))
    count = 1
    for i in li:
        flag = 0
        while(n%i == 0):
            flag += 1
            n = n/i
        count = count * (flag+1)
    return count

def countOddDivisor(n):
    li = map(countDivisor, range(1, n+1))
    return len(filter(lambda x:  True if x%2==1 else False, li))

num = int(raw_input())
for i in xrange(num):
    print countOddDivisor(int(raw_input()))

