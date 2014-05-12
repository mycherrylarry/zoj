#!/usr/bin/env python
def firstClass(mile): return 2*mile
def businessClass(mile): return int(1.5*mile)
def economyClass(mile):
    if mile<500: return 500
    else: return mile


classes = {'F':firstClass, 'B':businessClass, 'Y':economyClass}
n = raw_input()
total = 0
while(n != '#'):
    while(n != '0'):
        li = n.split()
        total += (classes.get(li[3]))(int(li[2]))
        n = raw_input()
    n = raw_input()
    print total
    total = 0


