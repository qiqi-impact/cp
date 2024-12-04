from functools import cache
from collections import defaultdict, deque
import math

N = 1000
grid = [[0 for _ in range(N)] for _ in range(N)]

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        x, y = l.split(' -> ')
        a, b = [int(t) for t in x.split(',')]
        c, d = [int(t) for t in y.split(',')]
        if a == c:
            if b > d:
                b,d = d,b
            for j in range(b, d+1):
                grid[a][j] += 1
        elif b == d:
            if a > c:
                a,c = c,a
            for j in range(a, c+1):
                grid[j][b] += 1

ret = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] > 1:
            ret += 1
print(ret)