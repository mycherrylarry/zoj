#!/usr/bin/env python
"""
f(n) = f(n-1) + 1/2n
f(0) = 0
"""

def deck(n):
    if n == 0:
        return 0
    return deck(n-1) + 0.5/n

