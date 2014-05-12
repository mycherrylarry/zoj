#!/usr/bin/env python
import sys
i, total = 0, 0
for line in sys.stdin:
    i = i+1
    total = total + float(line.strip())
    if (i == 12):
        print "$%.2f" %(total/12)
        break
    
