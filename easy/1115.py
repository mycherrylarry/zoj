#!/usr/bin/env python
import sys
for line in sys.stdin:
    num = int(line.strip())
    if num == 0:
        break
    while(num/10 != 0):
        tmp = 0
        while(num/10 != 0):
            tmp = tmp + num%10
            num = num/10
        num = tmp + num
    print num


