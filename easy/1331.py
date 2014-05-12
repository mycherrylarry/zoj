#!/usr/bin/env python
N = 200
b = [pow(i+1, 3) for i in range(200)]
c = [pow(i+1, 3) for i in range(200)]
d = [pow(i+1, 3) for i in range(200)]


for x in range(1,200):
    for i in range(1,200):
        for j in range(i,200):
            for k in range(j,200):
                if((b[i]+c[j]+d[k])==pow(x+1, 3)):
                    print "Cube = %d, Triple = (%d,%d,%d)" %(x+1, i+1, j+1, k+1)


