#!/usr/bin/env python

scoring_matrix = [
        [5,-1,-2,-1,-3],
        [-1,5,-3,-2,-4],
        [-2,-3,5,-2,-2],
        [-1,-2,-2,5,-1],
        [-3,-4,-2,-1,0]
]

def gene(la, lb):
    mp = {'A':0, 'C':1, 'G':2, 'T':3, '-':4}
    na, nb = len(la), len(lb)
    route = [[0 for col in range(na+1)] for raw in range(nb+1)]
    #init
    route[0][0] = 0
    for i in range(1, na+1):
        route[0][i] = scoring_matrix[4][mp[la[i-1]]] + route[0][i-1]
    for i in range(1, nb+1):
        route[i][0] = scoring_matrix[mp[lb[i-1]]][4] + route[i-1][0]

    for i in range(1, nb+1):
        for j in range(1, na+1):
            v1 = route[i-1][j-1] + scoring_matrix[mp[lb[i-1]]][mp[la[j-1]]]
            v2 = route[i][j-1] + scoring_matrix[mp[lb[i-1]]][4]
            v3 = route[i-1][j] + scoring_matrix[4][mp[la[j-1]]]
            route[i][j] = max(v1, v2, v3)
    return route

for i in  gene(list('AGCTTTAAA'), list('AGCTATT')):
    print i
