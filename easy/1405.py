#!/usr/bin/env python
def tanningSalon(n, li):
    s = set()
    rs = set()
    for item in li:
        if len(s)==0:
            s.add(item)
        elif len(s) < n:
            if item not in s:
                s.add(item)
            else:
                s.remove(item)
        else:
            if item not in s:
                rs.add(item)
            else:
                s.remove(item)

    if len(rs) == 0:
        print "All customers tanned successfully."
    else:
        print "%d customer(s) walked away." %len(rs)

        
line = raw_input()
while line != '0':
    li = line.split()
    tanningSalon(int(li[0]), list(li[1]))
    line = raw_input()
