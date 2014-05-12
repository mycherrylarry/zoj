#!/usr/bin/env python

def convertCharToInt(c):
    if ord(c)>= ord('A'):
        return ord(c)-ord('A')+10
    return int(c)

def convertIntToChar(i):
    if i >= 10:
        return chr(ord('A')+i-10)
    return chr(ord('0')+i)

# Convert X based numbers to decimal
def convertXToDecimal(li, x):
    return reduce(lambda a, b: x*a+b, [convertCharToInt(c) for c in li])

def convertDecimalToX(num, x):
    li = [num]
    while li[0]>=x:
        li.insert(0, li[0]/x)
        li[1] = li[1]%x
    return [convertIntToChar(i) for i in li]

import sys
for line in sys.stdin:
    params = line.split()
    decimal = convertXToDecimal(list(params[0]), int(params[1]))
    target = convertDecimalToX(decimal, int(params[2]))
    if len(target)>7:
        print "ERROR".rjust(7)
    else:
        print "".join(target).rjust(7)
