from functools import cache
from collections import defaultdict, deque
import math
from itertools import pairwise

D = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if i != 0 or j != 0:
            D.append((i, j))
# print(D)

g = []

class Octo:
    def __init__(self, e):
        self.e = e
        self.f = False

def prt():
    for i in range(R):
        s = ''
        for j in range(C):
            s += str(g[i][j].e)
        print(s)

ret = 0
R = 0
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        R += 1
        C = len(l)
        g.append([Octo(int(x)) for x in l])

for _ in range(100):
    for i in range(R):
        for j in range(C):
            g[i][j].e += 1
    q = []
    for i in range(R):
        for j in range(C):
            if g[i][j].e == 10:
                q.append((i, j))
                g[i][j].f = True
                ret += 1

    qp = 0
    while qp < len(q):
        x, y = q[qp]
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            # print(nx, ny)
            if 0 <= nx < R and 0 <= ny < C:
                g[nx][ny].e += 1
                if g[nx][ny].e == 10:
                    q.append((nx, ny))
                    g[nx][ny].f = True
                    ret += 1
        qp += 1

    for i in range(R):
        for j in range(C):
            if g[i][j].f:
                g[i][j].e = 0
                g[i][j].f = False
    
    # prt()
    # input()

print(ret)