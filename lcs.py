#!/usr/bin/env python

def lcs(lia, lib):
    na , nb = len(lia), len(lib)
    route = [[0 for cow in range(nb+1)] for row in range(na+1)]
    for i in range(1,na+1):
        for j in range(1,nb+1):
            if lia[i-1] == lib[j-1]:
                route[i][j] = route[i-1][j-1] + 1
            else:
                route[i][j] = max(route[i-1][j], route[i][j-1])
    return route

for item in  lcs(list('GCCCTAGCG'), list('GCGCAATG')):
    print item

