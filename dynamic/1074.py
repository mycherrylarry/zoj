#!/usr/bin/env python

def dynamic(li, n):
    route = [[0 for col in range(n+1)] for raw in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            tmp = [[0 for col in range(j+1)] for raw in range(i+1)]
            for x in range(i-2, -1, -1):
                for y in range(j-2, -1, -1):
                    print li[x:i-1][y]
                    tmp[x][y] = tmp[x][y+1] + sum(li[x:(i-1)][y])
            max_with_current_token = max([max(item) for item in tmp])
            route[i][j] = max(route[i-1][j], route[i][j-1], max_with_current_token)
    return route

print dynamic([[0,-2],[9,2]], 2)


