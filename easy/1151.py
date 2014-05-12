#!/usr/bin/env python
import sys
while True:
    num = int(raw_input())
    for i in range(num):
        li = raw_input().split()
        print " ".join([x[::-1] for x in li])

