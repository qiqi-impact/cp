from functools import cache
from collections import defaultdict, deque
import math
from itertools import pairwise

D = list(pairwise([1, 0, -1, 0, 1]))

g = []

R = 0
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        R += 1
        C = len(l)
        g.append([int(x) for x in l])

lp = []

for i in range(R):
    for j in range(C):
        fail = False
        for dx, dy in D:
            nx, ny = i+dx, j+dy
            if 0 <= nx < R and 0 <= ny < C and g[nx][ny] <= g[i][j]:
                fail = True
                break
        if not fail:
            lp.append((i, j))

def bfs(p):
    q = [p]
    seen = set(q)
    qp = 0
    while qp < len(q):
        x, y = q[qp]
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in seen and g[nx][ny] > g[x][y] and g[nx][ny] != 9:
                q.append((nx, ny))
                seen.add((nx, ny))
        qp += 1
    return len(q)

r = []
for p in lp:
    r.append(bfs(p))
r.sort()
print(math.prod(r[-3:]))