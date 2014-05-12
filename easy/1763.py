#!/usr/bin/env python

num = raw_input()
flag, pre = 0, 0
while num!='999':
    if flag == 0:
        flag = 1
        pre = float(num)
    else:
        cur = float(num)
        print "%.2f" %(cur-pre)
        pre = cur
    num = raw_input()

print "End of Output"




