from functools import cache
from collections import defaultdict, deque
import math
from itertools import pairwise

D = list(pairwise([1, 0, -1, 0, 1]))

g = []

ret = 0
R = 0
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        R += 1
        C = len(l)
        g.append([int(x) for x in l])

for i in range(R):
    for j in range(C):
        fail = False
        for dx, dy in D:
            nx, ny = i+dx, j+dy
            if 0 <= nx < R and 0 <= ny < C and g[nx][ny] <= g[i][j]:
                fail = True
                break
        if not fail:
            ret += 1 + g[i][j]

print(ret)