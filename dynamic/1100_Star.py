#!/usr/bin/env python
"""
经典的覆盖题目，内容涉及到状态压缩＋动态规划。思路如下：
设：H为层数（Hight），W为列数（Width），MAX为最大列数，tran[1<<MAX][2]为二维数组，存放所有可能的层排列方式(包括上下层),OP[H+1][1<<W]为二维数组，存储状态结果。
初始条件：OP[0][(1<<W)-1] = 1 
       /* 设W=6,则(1<<W)-1 = '111111', 由于OP[1]['111111']只有一种状态，即砖块全部横铺，所以按照
          OP[i+1][tran[j][down]] += OP[i][tran[j][up]] => OP[1]['111111'] += OP[0]['111111'] => OP[1]['111111']=1  */
求：OP[H][1<<W - 1]
"""

"""
H, W = 2,11
tran = []
def dfs(n, up, down):
    if n > W:
        return
    if n == W:
        tran.append([up, down])
        return
    dfs(n+2, (up<<2)+3, (down<<2)+3) # because 3 = '0b11'
    dfs(n+1, (up<<1)+1, (down<<1))
    dfs(n+1, (up<<1), (down<<1)+1)


def dynamic():
    OP = [[0]*(1<<W) for t in range(H+1)]
    OP[0][(1<<W)-1] = 1
    for i in range(1, H+1):
        for j in range(len(tran)):
            OP[i][tran[j][1]] += OP[i-1][tran[j][0]]
    return OP

dfs(0,0,0)
OP = dynamic()
print OP[H][(1<<W)-1]
"""

class Brick:
    def __init__(self, (H, W)):
        self.H = H
        self.W = W
        self.tran = []
        self.OP = [[0]*(1<<W) for t in range(H+1)]

    def dfs(self, n, up, down):
        tran = self.tran
        H, W = self.H, self.W
        if n > W:
            return
        if n == W:
            tran.append([up, down])
            return
        self.dfs(n+2, (up<<2)+3, (down<<2)+3) # because 3 = '0b11'
        self.dfs(n+1, (up<<1)+1, (down<<1))
        self.dfs(n+1, (up<<1), (down<<1)+1)

    def dynamic(self):
        OP = self.OP
        tran = self.tran
        H, W = self.H, self.W
        OP[0][(1<<W)-1] = 1
        for i in range(1, H+1):
            for j in range(len(tran)):
                OP[i][tran[j][1]] += OP[i-1][tran[j][0]]

    def run(self):
        self.dfs(0,0,0)
        self.dynamic()
        return self.OP[self.H][(1<<(self.W))-1]

from operator import eq
li = [int(x) for x in raw_input().split()]
while not all(map(eq, li, [0,0])):
    brick = Brick(li)
    print brick.run()
    beautifyMArrayPrinter(brick.OP)
    li = [int(x) for x in raw_input().split()]
    
